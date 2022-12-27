# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 22:44:48 2022

@author: segar
"""

from datetime import datetime
import requests
import numpy as np
import json
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#https://query1.finance.yahoo.com/v8/finance/chart/%5EIXIC?symbol=%5EIXIC&period1=1664316000&period2=1664920800&useYfid=true&interval=1m&includePrePost=true&events=div%7Csplit%7Cearn&lang=es-ES&region=ES&crumb=SwbdaQw9MYL&corsDomain=es.finance.yahoo.com
#https://query1.finance.yahoo.com/v8/finance/chart/AAPL?symbol=AAPL&period1=1667943451&period2=1668116251&useYfid=true&interval=1m&includePrePost=true&events=div|split|earn&lang=es-ES&region=ES&crumb=SwbdaQw9MYL&corsDomain=es.finance.yahoo.com

date_string_1 = "1 December, 2022"
date_string_2 = "2 December, 2022"


date_object = datetime.strptime(date_string_1, "%d %B, %Y")
timestamp_1 = int(datetime.timestamp(date_object))
date_object = datetime.strptime(date_string_2, "%d %B, %Y")
timestamp_2 = int(datetime.timestamp(date_object))
# timestamp_2_2 = timestamp_1 + 604800

# resp = requests.get('https://tvc4.investing.com/25bb9d3d09dcde4f698aae33d569f7a7/1668119234/4/4/58/history?symbol=6408&resolution=1&from=1651096800&to=1651183200')


# d = np.load('Nasdaq1week.txt').tojson

# import json
  
# # Opening JSON file
# f = open('Nasdaq1week.txt')
  
# # returns JSON object as 
# # a dictionary
# data = json.load(f)
# f.close()
#%%


# Definimos la URL-principal y la ruta al driver de chrome
main_url = 'https://query1.finance.yahoo.com/v8/finance/chart/AAPL?symbol=AAPL&period1=' + str(timestamp_1) + '&period2=' + str(timestamp_2) + '&useYfid=true&interval=1m&includePrePost=true&events=div|split|earn&lang=es-ES&region=ES&crumb=SwbdaQw9MYL&corsDomain=es.finance.yahoo.com' 
chromedriver = './chromedriver'
# Abrimos una ventana con la URL-principal
driver= webdriver.Chrome(chromedriver)
driver.get(main_url)
Body = driver.find_element(By.XPATH, "/html/body").text

Body_json = json.loads(Body)

price_high = np.array(Body_json["chart"]["result"][0]["indicators"]["quote"][0]["high"],'float')
price_low = np.array(Body_json["chart"]["result"][0]["indicators"]["quote"][0]["low"],'float')
price_open = np.array(Body_json["chart"]["result"][0]["indicators"]["quote"][0]["open"],'float')
price_close = Body_json["chart"]["result"][0]["indicators"]["quote"][0]["close"]
volume = np.array(Body_json["chart"]["result"][0]["indicators"]["quote"][0]["volume"],'float')
timestamp = Body_json["chart"]["result"][0]["timestamp"]
time.sleep(2)
driver.close()

plt.plot(timestamp, price_close)
plt.show()


