# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 20:04:35 2022

@author: segar


"""

import csv
import requests
import time
import pickle  

apikey = 'SJAUMLEO3J3YKXE6'
data = dict()

NASDAQ100 = ['ATVI',
'ADBE',
'AMD',	
'ALXN',
'ALGN',
'GOOG',
'AMZN',
'AAL',	
'AMGN',
'ADI',	
'AAPL',
'AMAT',
'ASML',
'ADSK',
'ADP',	
'BIDU',
'BIIB',
'BMRN',
'BKNG',
'AVGO',
'CDNS',
'CELG',
'CERN',
'CHTR',
'CHKP',
'CTAS',
'CSCO',
'CTXS',
'CTSH',
'CMCS',
'COST',
'CSX',	
'CTRP',
'DLTR',
'EBAY',
'EA',
'EXPE',
'FB',
'FAST',
'FISV',
'FOX,',
'GILD',
'HAS',	
'HSIC',
'IDXX',
'ILMN',
'INCY',
'INTC',
'INTU',
'ISRG',
'JBHT',
'JD',
'KLAC',
'LRCX',
'LBTY',
'LULU',
'MAR',	
'MXIM',
'MELI',
'MCHP',
'MU',
'MSFT',
'MDLZ',
'MNST',
'MYL',	
'NTAP',
'NTES',
'NFLX',
'NVDA',
'NXPI',
'ORLY',
'PCAR',
'PAYX',
'PYPL',
'PEP',	
'QCOM',
'REGN',
'ROST',
'SIRI',
'SWKS',
'SBUX',
'SYMC',
'SNPS',
'TTWO',
'TSLA',
'TXN',	
'KHC',	
'TMUS',
'ULTA',
'UAL',	
'VRSN',
'VRSK',
'VRTX',
'WBA',	
'WDC',	
'WLTW',
'WDAY',
'WYNN',
'XEL',	
'XLNX']

IBEX = ['ANA' ,
'ACX'  ,
'ACS'  ,
'AENA' ,
'AMS'  ,
'BBVA' ,
'SAB'  ,
'SAN'  ,
'BKT'  ,
'CABK' ,
'CLNX' ,
'ENG'  ,
'ELE'  ,
'FER'  ,
'GRF'  ,
'IBE'  ,
'IDR'  ,
'ITX'  ,
'IAG'  ,
'MAP'  ,
'TL5'  ,
'MEL'  ,
'MRL'  ,
'NTGY' ,
'RED'  ,
'REP'  ,
'SGRE' ,
'TRE'  ,
'TEF'  ,
'VIS']

for symbol in IBEX:
    print(symbol)
    prices = []
    for year in range(1,3):
        for month in range(1,13):
            CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=' + symbol +'&interval=1min&slice=year'+str(year)+'month'+str(month)+'&apikey='+ apikey
    
            with requests.Session() as s:
                download = s.get(CSV_URL)
                decoded_content = download.content.decode('utf-8')
                cr = csv.reader(decoded_content.splitlines(), delimiter=',')
                my_list = list(cr)
            prices = prices + my_list
            time. sleep(13)


    data[symbol] = prices
    a_file = open(symbol+".pkl", "wb")
    pickle.dump(data[symbol], a_file)
    a_file.close()
    
 

    
 

 
    