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
        return df
    
    @staticmethod
    def compute_sma(df, period=50):
        df["sma50_close"]=ta.sma(df["close"], length = period)
        return df