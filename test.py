# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.dates as mdates
import datetime as dt
import pandas_datareader.data as web

style.use('ggplot')

# =============================================================================
#control 4 makes it quotes 
start = dt.datetime(2000,1,1)

df = pd.read_csv('tsla.csv', parse_dates = True, index_col=0)

#df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)
print(df_ohlc.head())


print(df_ohlc.head())

ax1 = plt.subplot2grid((6,1),(0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1),(5,0), rowspan=1, colspan=1, sharex=ax1)


#plt.show()



# end = dt.datetime(2016,12,31)
# 
# df = web.DataReader('TSLA', 'yahoo', start, end)
# =============================================================================

# =============================================================================
# print(df.head())
# =============================================================================

# =============================================================================
# print(df[['Open', 'High']].head)
# 
# df['Adj Close'].plot()
# plt.show()
# =============================================================================
