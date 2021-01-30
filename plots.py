#%%
from pathlib import Path
import pandas as pd
import hvplot.pandas

#read in dataframe
data_df = pd.read_csv(Path("C:/users/etliv/Documents/join_data.csv"), index_col="Ticker")


#Creating dataframe with unique ticker row & information
summary_df = data_df.drop(columns=['Date'])
unique_sum_df = summary_df.reset_index().drop_duplicates(subset='Ticker',keep='first').set_index('Ticker')

#Plotting Top Earnings Growth YOY Companies
quart_earnings_df = unique_sum_df.sort_values('QuarterlyEarningsGrowthYOY',ascending=False)
top_earnings_df = quart_earnings_df.head(15)
#top_unique_df.head(10)
top_earnings_df.hvplot.barh(x='Ticker', y='QuarterlyEarningsGrowthYOY',flip_yaxis=True)


#Plotting Top Earnings Per Share Companies
eps_df = unique_sum_df.sort_values('EPS',ascending=False)
top_eps_df = eps_df.head(15)
top_eps_df.hvplot.barh(x='Ticker', y='EPS',flip_yaxis=True)

#Plotting Top Earnings Per Share Sectors
top_eps_df.hvplot.barh(x='Sector', y='EPS',flip_yaxis=True)

#Plotting Top Profit Margin Sectors
pm_df = unique_sum_df.sort_values('ProfitMargin',ascending=False)
top_pm_df = pm_df.head(15)
top_pm_df.hvplot.barh(x='Sector', y='ProfitMargin',flip_yaxis=True)

#Plotting Top Quarterly Revenue Sectors
revenue_df = unique_sum_df.sort_values('QuarterlyRevenueGrowthYOY',ascending=False)
top_revenue_df = revenue_df.head(15)
top_revenue_df.hvplot.barh(x='Sector', y='QuarterlyRevenueGrowthYOY',flip_yaxis=True)





