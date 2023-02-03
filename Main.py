# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 22:44:48 2022

@author: segar


Modes:
    1- Take and clean Data from Alpha Vantage Api
    2- Analize data, add indicators
    3- Simulate strategy
    4- Optimize strategy
    5- Real time signals



"""

from Analize_symbol import Analize_symbol, Represent_symbol
import Calculate_indicator 

mode = 2
args = "AAL.pkl"



def mode_1():
    df = Analize_symbol.create_symbol_dataset(args)
    print(df)
    

def mode_2():    
    df = Calculate_indicator.Calculate_indicator.compute_rsi(df)
    Analize_symbol.represent_symbol("close","rsi_close",period_ini = "01-01-2022", perid_end = "01-02-2022")
    


switch_mode = {
    1: mode_1,
    2: mode_2
        }

switch_mode.get(mode)