""" Simulator module"""

import sys
from datetime import datetime as dt
import time

class Simulator():

    def __init__(self, budget, strategy="rsi", quantity=5, fixed_comission=0, variable_comission=0.01, min_tax=4) -> None:
        """
        Inputs:
            - budget: Initial capital
            - strategy: Strategy to follow
            - quantity: Number of stocks to buy
            - fixed_comission: Fixed comission (absolute value)
            - variable_comission: Variable order comission (absolute value, not percentage)
            - min_tax: Minimum order comission.
        """
        self.budget = budget
        self.strategy = strategy
        self.quantity = quantity
        self.n_stocks = 0
        self.fixed_comission = fixed_comission
        if variable_comission >= 1:
            msg = "\n"+"#"*100 + f"\n\nERROR: Variable comission must be set as a number not percentage.\nPLease, try {variable_comission/100} instead" 
            exit(msg)
        self.variable_comission = variable_comission
        self.min_tax = min_tax
    
    def run_simulation(self, data, date_ini, date_end):

        format = "%d-%m-%Y"
        start_time = dt.strptime(date_ini, format)
        final_time = dt.strptime(date_end, format)
        data = data[data["unix"]>=time.mktime(start_time.timetuple())]
        data = data[data["unix"]<=time.mktime(final_time.timetuple())]

        data = self.change_index(data)
        for idx in range(data.shape[0]):
            order = self.strategy.perform(data.loc[idx])         
            if order == "buy":
                self.buy_position(data["close"].loc[idx])
                #print(f"\n\n RSI: {data['rsi_close'].loc[idx]} || Order: {order} || Price: {data.close.loc[idx]} || N_Stocks: {self.n_stocks} || Budget: {self.budget}")
            if order == "sell":
                self.sell_position(data["close"].loc[idx])
                #print(f"\n\n RSI: {data['rsi_close'].loc[idx]} || Order: {order} || Price: {data.close.loc[idx]} || N_Stocks: {self.n_stocks} || Budget: {self.budget}")
            # if data["rsi_close"].loc[idx] < 20 or data["rsi_close"].loc[idx] > 70:


    def buy_position(self, stock_price):
        taxes = self.compute_total_taxes("buy", stock_price)
        if self.budget >= self.quantity*stock_price + taxes:
            self.budget = self.budget - self.quantity*stock_price - taxes
            self.n_stocks = self.n_stocks+self.quantity
            print(f"\n\n Order: buy || Price: {stock_price} || N_Stocks: {self.n_stocks} || Budget: {self.budget}")
        # else:
        #     sys.exit("No budget available")
    
    def sell_position(self, stock_price):
        if self.n_stocks > 0:
            taxes = self.compute_total_taxes("sell",stock_price)
            self.budget = self.budget + self.n_stocks*stock_price - taxes
            self.n_stocks = 0
            print(f"\n\n Order: sell || Price: {stock_price} || N_Stocks: {self.n_stocks} || Budget: {self.budget}")

    def change_index(self,data):
        if data.index.name == "time":
            data.reset_index(drop=True, inplace=True)
        return data
    
    def compute_total_taxes(self, order, stock_price):
        if order=="buy":
            total = self.quantity * stock_price * self.variable_comission + self.fixed_comission
        
        if order == "sell":
            total = self.n_stocks*stock_price*self.variable_comission + self.fixed_comission
        
        if total > self.min_tax:
            total = self.min_tax
        
        return total
        