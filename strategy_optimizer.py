# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 20:33:43 2023

@author: segar
"""

from scipy import optimize
from analize_symbol import Analize_symbol
from simulator import Simulator
from strategies import rsi, rsi_macd



def function_profit(x):
    budget = 1000
    quantity = x[0]
    strategy = rsi(x[1],x[2])

    
    simulator = Simulator(budget, strategy, quantity, fixed_comission=1, variable_comission=0, min_tax=1)
    simulator.run_simulation(data, "25-01-2021", "25-02-2021")
    print(simulator.budget)
    return -simulator.budget

def function_profit_rsi_macd(x):
    budget = 10000
    quantity = 500
    strategy = rsi_macd(value_buy=x[0], value_sell=x[1], period_rsi = int(x[2]), period_mean_rsi=int(x[3]), fast_macd = int(x[4]), slow_macd = int(x[5]), take_profit = x[6], stop_loss = x[7])
    strategy.calculate_indicators(data)

    
    simulator = Simulator(budget, strategy, quantity, fixed_comission=1, variable_comission=0, min_tax=1)
    simulator.run_simulation(data, "25-01-2021", "25-02-2021")
    print(simulator.budget)
    return -simulator.budget

x0 = [20,70,14,14,9,14,0.01,-0.01]
data = Analize_symbol.create_symbol_dataset("AAL")





bounds = optimize.Bounds(lb=[5,60,5,5,5,5,0.005,-0.03], ub=[40,90,30,50,30,50,0.03,-0.001])

#xopt = optimize.minimize(function_profit_rsi_macd, x0, args=(),  bounds=bounds,  tol=1, callback=None, options={'disp':True})



xopt = optimize.differential_evolution(function_profit_rsi_macd, bounds = bounds, maxiter=30, popsize=15, tol=1,  disp=True, atol=0)

