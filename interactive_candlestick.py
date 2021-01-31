#%%
import plotly.graph_objects as go
import hvplot.pandas
import pandas as pd
from datetime import datetime
import panel as pn
from panel.interact import interact
from panel import widgets
pn.extension()

df = pd.read_csv('~/Documents/project_ticker_data.csv')
ticker_list = df['ticker'].drop_duplicates()

#def choose_ticker(ticker):

#ticker_list
#interact(choose_year, year=list_of_years_2)

def plot_candlestick_chart(ticker):
    df = pd.read_csv('~/Documents/project_ticker_data.csv')
    df.drop(columns=['Unnamed: 0'],inplace=True)
    df.set_index('ticker',inplace=True)
    ticker_df = df.loc[ticker]
    fig = go.Figure(data=[go.Candlestick(x=ticker_df['Date'],
    open=ticker_df['Open'],
    high=ticker_df['High'],
    low=ticker_df['Low'],
    close=ticker_df['Close'])])
    #fig.show()
    return fig.show()

#plot_candlestick_chart('INTC')
interact(plot_candlestick_chart, ticker = ['INTC','AAPL'] )
# %%
