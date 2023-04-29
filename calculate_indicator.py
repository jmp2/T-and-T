# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 20:53:41 2023

@author: segar
"""

import pandas_ta as ta
import pandas as pd
import numpy as np

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
        df["cross_macd"] = False
        condition_1 = df["macdh_close"].shift(1)<0.04
        condition_2 = df["macdh_close"]>0.04
        df["cross_macd"][condition_1 * condition_2] = True
                    
                
        return df
    
    @staticmethod
    def compute_sma(df:pd.DataFrame, period=50):
        df["sma_"+ str(period) + "_close"]=ta.sma(df["close"], length = period)
        return df
    
    @staticmethod
    def compute_mean_rsi(df:pd.DataFrame, period=5):
        df["mean_rsi_close"]=ta.sma(df["rsi_close"], length = period)
        df["derivative_mean_rsi_close"] = np.insert(np.diff(df["mean_rsi_close"]), 0, 0)
        df["derivative_mean_rsi_close"] = ta.sma(df["derivative_mean_rsi_close"], length=3)
        
        df["2_derivative_mean_rsi_close"] = np.insert(np.diff(df["derivative_mean_rsi_close"]), 0, 0)
        df["2_derivative_mean_rsi_close"] = ta.sma(df["2_derivative_mean_rsi_close"], length=3)
        
        return df