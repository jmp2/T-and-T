# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 12:39:37 2022

@author: segar
"""

import pandas as pd
import matplotlib.pyplot as plt
import pickle
import numpy as np
from datetime import datetime as dt


class Analize_symbol():

    @staticmethod
    def create_symbol_dataset (symbol):
    
    
        data = pd.read_pickle("./"+symbol+'.pkl')
        
                    
        df = pd.DataFrame(data[1:],columns=data[0][:])
        df_ = df[df["time"]!="time"]
        formato = "%Y-%m-%d %H:%M:%S"
        df_["time"] = pd.to_datetime(df_['time'], format=formato)
        
        df_.set_index(pd.DatetimeIndex(df_["time"]), inplace=True)
        df_.sort_index(inplace=True)
        df_["open"] = df_["open"].astype(float)
        df_["high"] = df_["high"].astype(float)
        df_["low"] = df_["low"].astype(float)
        df_["close"] = df_["close"].astype(float)
        df_["unix"] = pd.to_datetime(df_['time']).astype(np.int64)/10**9
        
        df_["hour"] = df_["time"].dt.time
        start_time = "09:30:00"
        final_time = "16:00:00"
        format = "%H:%M:%S"
        start_time = "09:30:00"
        final_time = "16:00:00"
        start_time = dt.strptime(start_time, format)
        final_time = dt.strptime(final_time, format)
        df_ = df_[df_["hour"]>=start_time.time()]
        df_ = df_[df_["hour"]<=final_time.time()]
        df_["time_difference"] = df_["unix"].diff()
    
        
        return df_
    

    # @staticmethod
    # def Represent_symbol (columns):
        


