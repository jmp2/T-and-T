# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 20:53:41 2023

@author: segar
"""

import pandas_ta as ta
import pandas as pd

class Calculate_indicator():
    @staticmethod
    def compute_rsi(df:pd.DataFrame, period=14):
        df["rsi_close"]=ta.rsi(df["close"], length = period)
        return df
    
    @staticmethod
    def compute_macd(df:pd.DataFrame, fast=8, slow=21):
        df[["macd_close", "macdh_close", "macds_close"]] = ta.macd(
                                                                df["close"],
                                                     slow = slow)
        df["cross_macd"] = df["macd_close"]
               
        for i in range(1,len(df)):
            if (df["macd_close"][i-1] < 0 and df["macd_close"][i]>0):
                df["cross_macd"][i] = 1
            else:
                df["cross_macd"][i] = 0
                    
                
        return df
    
    @staticmethod
    def compute_sma(df:pd.DataFrame, period=50):
        df["sma"+ str(period) + "_close"]=ta.sma(df["close"], length = period)
        return df
    
    @staticmethod
    def compute_mean_rsi(df:pd.DataFrame, period=5):
        df["mean_rsi_close"]=ta.sma(df["rsi_close"], length = period)
        return df