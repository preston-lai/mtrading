from  datetime import datetime
import backtrader as bt 
import pandas as pd
import yfinance as yf
import matplotlib.dates

#define strategy as a class
#This is a general backtrader strategy -> change the indicator of 50 and not a simple crossover) 
class SMACross(bt.SignalStrategy): 
    def __init__(self): 
        sma1, sma2 = bt.ind.SMA(period=10), bt.ind.SMA(period=30)
        crossover = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(bt.SIGNAL_LONG, crossover)
        
cerebro = bt.Cerebro()
cerebro.addstrategy(SMACross)

#Getting data from Yahoo, can be used from bt functions (Jan 1)
#Note: BTC-USD not found, need to change it to a csv
data = bt.feeds.PandasData(dataname=yf.download('BTC-USD', '2018-01-01', '2022-01-01'))

cerebro = bt.Cerebro()
cerebro.adddata(data)
cerebro.run()
cerebro.plot()
