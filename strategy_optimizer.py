# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 20:33:43 2023

@author: segar
"""

from scipy import optimize
from analize_symbol import Analize_symbol
from calculate_indicator import Calculate_indicator
from simulator import Simulator
from strategies import rsi



def function_profit(x):
    budget = 1000
    quantity = x[0]
    strategy = rsi(x[1],x[2])

    
    simulator = Simulator(budget, strategy, quantity)
    simulator.run_simulation(df, "25-01-2021", "25-02-2021")
    print(simulator.budget)
    return -simulator.budget

x0 = [10, 40, 60]


df = Analize_symbol.create_symbol_dataset("AAL")
Calculate_indicator.compute_rsi(df)




bounds = optimize.Bounds(lb=[5,0,0], ub=[70,100,100])

#xopt = optimize.minimize(function_profit, x0, args=(), method='SLSQP',  bounds=bounds,  tol=0.1, callback=None, options={'disp':True})



xopt = optimize.differential_evolution(function_profit, bounds = bounds, maxiter=1000, popsize=15, tol=0.1,  disp=True, atol=0)

