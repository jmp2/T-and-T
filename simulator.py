""" Simulator module"""

import sys
from datetime import datetime as dt
import time

class Simulator():

    def __init__(self, budget, strategy="rsi", quantity=5) -> None:
        self.budget = budget
        self.strategy = strategy
        self.quantity = quantity
        self.n_stocks = 0
    
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
        if self.budget >= self.quantity*stock_price:
            self.budget = self.budget - self.quantity*stock_price
            self.n_stocks = self.n_stocks+self.quantity
            print(f"\n\n Order: buy || Price: {stock_price} || N_Stocks: {self.n_stocks} || Budget: {self.budget}")
        # else:
        #     sys.exit("No budget available")
    
    def sell_position(self, stock_price):
        if self.n_stocks > 0:
            self.budget = self.budget + self.n_stocks*stock_price
            self.n_stocks = 0
            print(f"\n\n Order: sell || Price: {stock_price} || N_Stocks: {self.n_stocks} || Budget: {self.budget}")

    def change_index(self,data):
        if data.index.name == "time":
            data.reset_index(drop=True, inplace=True)
        return data