# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 12:39:37 2022

@author: segar
"""

import pandas as pd
import matplotlib.pyplot as plt
import pickle



a_file = open("AAL.pkl", "rb")
symbol = pickle.load(a_file)    
a_file.close()    
    


df = pd.DataFrame(symbol)
df.columns = symbol[0]
df = df[df.time != 'time']
df.time = pd.to_datetime(df.time, format='%Y-%m-%d %H:%M:%S.%f')


plt.plot(df.time,df.close)
plt.show()