#%%
import plotly.graph_objects as go

import pandas as pd
from datetime import datetime


df = pd.read_csv('C:/users/etliv/Documents/project_ticker_data.csv')

df.set_index('ticker',inplace=True)
df.drop(columns=['Unnamed: 0'],inplace=True)
intc_df = df.loc['INTC']
fig = go.Figure(data=[go.Candlestick(x=intc_df['Date'],
open=intc_df['Open'],
high=intc_df['High'],
low=intc_df['Low'],
close=intc_df['Close'])])
fig.show()
# %%

# %%

# %%
