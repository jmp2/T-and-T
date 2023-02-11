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

from analize_symbol import Analize_symbol
from calculate_indicator import Calculate_indicator
from simulator import Simulator
from strategies import rsi

mode = 2
args = "AAL"
budget = 1000
quantity = 60
strategy = rsi(30,70)

date_ini = "25-01-2021"
date_end = "27-03-2021"

df = Analize_symbol.create_symbol_dataset(args)
Calculate_indicator.compute_rsi(df)
Calculate_indicator.compute_sma(df, 100)

#Analize_symbol.represent_symbol(df, ["close","rsi_close", 'sma100_close'], date_ini = "25-01-2021", date_end = "26-01-2021")

simulator = Simulator(budget, strategy, quantity, variable_comission=0.01)
simulator.run_simulation(df, date_ini, date_end)

Analize_symbol.represent_symbol(df, ["close","rsi_close"], date_ini=date_ini, date_end =date_end)
# def mode_1():
#     df = Analize_symbol.create_symbol_dataset(args)
#     print(df)
    

# def mode_2():    
#     df = Calculate_indicator.Calculate_indicator.compute_rsi(df)
#     Analize_symbol.represent_symbol("close","rsi_close",period_ini = "01-01-2022", perid_end = "01-02-2022")
    


# switch_mode = {
#     1: mode_1,
#     2: mode_2
#         }

# switch_mode.get(mode)