import pandas as pd
import yfinance as yf
import time
ticker_df = {}
start_date = '2019-01-01'
end_date = '2021-01-23'

short_ticker_list = ['NLOK','XRX','SNX','NCR','INTC','COHR','QCOM','JBL','PTC','FSLR','GRWG','OGI','EGOV','CGC','HEXO','AMRS','APHA','TRPXY','CRON','CGC','VW','LNG','OKE','OKE','WMB','EQT','CVX','VLO','TGE','XOM','MUR','UNM','VIRT','AFL','WTM','KKR','AFL','PYPL','SIVB','VIRL','XLF','EAF','AL','MAS','ROK','AGCO','VRSK','GNRC','AAXN','SPCE','3MM']
#for loop for iterating through ticker list
for ticker in short_ticker_list:
    print(f'Checking Data for Ticker {ticker}')
    #statement for continuing loop in the case of an error from Yahoo Finance Package & getting ticker symbol data
    try: 
        data_df = yf.download(ticker, start=start_date, end=end_date)
        data_df['ticker'] = ticker
        data_df.reset_index(inplace=True)
        #Include the header on the 1st file write 
        if short_ticker_list.index(ticker) == 0:
            mode = None
            header = True
        #ignoring header on subsequent writes
        else:
            mode = 'a'
            header = False
        #writing dataframe to csv
        data_df.to_csv('project_ticker_data.csv',mode='a',header=header)
        time.sleep(2)
        
    except:
        print(f'Data for ticker: {ticker} is not available')
        pass
