import requests
import pandas as pd
import locale

#setting intial variables & conditions
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )
url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-financials"
headers = {'x-rapidapi-key': "0aacde98f1msh7d59ebf2c730db9p1bcae5jsn533514050ec8",'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"}
data_rows = {'ticker':['q4y1_gross_profit','q4y1_total_revenue','q4y1_earnings_estimate','q3y1_gross_profit','q3y1_total_revenue', 'q3y1_earnings','q2y1gross_profit','q2y1_total_revenue','q2y1_earnings']}
short_ticker_list = ['NLOK','XRX','SNX','NCR','INTC','COHR','QCOM','JBL','PTC','FSLR','GRWG','OGI','EGOV','CGC','HEXO','AMRS','APHA','TRPXY','CRON','CGC','VW','LNG','OKE','OKE','WMB','EQT','CVX','VLO','TGE','XOM','MUR','UNM','VIRT','AFL','WTM','KKR','AFL','PYPL','SIVB','VIRL','XLF','EAF','AL','MAS','ROK','AGCO','VRSK','GNRC','AAXN','SPCE','3MM']

ticker = 'NLOK'
for ticker in short_ticker_list:
    print(f'Checking Data for Ticker {ticker}')
    try:
        querystring = {"symbol":ticker,"region":"US"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        print(f'Entering value {ticker} index information ')
        
        #Pull 4th quarter financial data current year
        q4y1_gross_profit = locale.atof(data['incomeStatementHistoryQuarterly']['incomeStatementHistory'][0]['grossProfit']['longFmt'])
        q4y1_total_revenue = locale.atof(data['incomeStatementHistoryQuarterly']['incomeStatementHistory'][0]['totalRevenue']['longFmt'])
        q4y1_earnings_estimate = locale.atof(data['earnings']['earningsChart']['currentQuarterEstimate']['fmt'])
        
        #Pull 3rd Quarter financial data current year
        q3y1_gross_profit = locale.atof(data['incomeStatementHistoryQuarterly']['incomeStatementHistory'][1]['grossProfit']['longFmt'])
        q3y1_total_revenue = locale.atof(data['incomeStatementHistoryQuarterly']['incomeStatementHistory'][1]['totalRevenue']['longFmt'])
        q3y1_earnings = locale.atof(data['earnings']['financialsChart']['quarterly'][3]['earnings']['longFmt'])
        
        #Pull 2nd Quarter financial data current year
        q2y1gross_profit = locale.atof(data['incomeStatementHistoryQuarterly']['incomeStatementHistory'][2]['grossProfit']['longFmt'])
        q2y1_total_revenue = locale.atof(data['incomeStatementHistoryQuarterly']['incomeStatementHistory'][2]['totalRevenue']['longFmt'])
        q2y1_earnings = locale.atof(data['earnings']['financialsChart']['quarterly'][2]['earnings']['longFmt'])
        
        #appending the dictionary
        data_rows[ticker] = [q4y1_gross_profit,q4y1_total_revenue,q4y1_earnings_estimate,q3y1_gross_profit,q3y1_total_revenue,q3y1_earnings,q2y1gross_profit,q2y1_total_revenue,q2y1_earnings]
        
    except:
        print(f'Ticker {ticker} is not available')
        pass
    
    df = pd.DataFrame.from_dict(data_rows, orient="index")
    df.to_csv("ticker_info.csv")
    
