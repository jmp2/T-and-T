""" Simulator module"""
from strategies import Strategies
import sys

class Simulator():

    def __init__(self, budget, strategy="rsi", quantity=5) -> None:
        self.budget = budget
        self.strategy = strategy
        self.quantity = quantity
        self.n_stocks = 0
    
    def run_simulation(self, data):
        data = data[0:1000]
        data = self.change_index(data)
        for idx in range(data.shape[0]):
            order = Strategies.rsi_strategy(data["rsi_close"].loc[idx])
            if order == "buy":
                self.buy_position(data["close"].loc[idx])
                print(f"\n\n RSI: {data['rsi_close'].loc[idx]} || Order: {order} || Price: {data.close.loc[idx]} || N_Stocks: {self.n_stocks} || Budget: {self.budget}")
            if order == "sell":
                self.sell_position(data["close"].loc[idx])
                print(f"\n\n RSI: {data['rsi_close'].loc[idx]} || Order: {order} || Price: {data.close.loc[idx]} || N_Stocks: {self.n_stocks} || Budget: {self.budget}")
            # if data["rsi_close"].loc[idx] < 20 or data["rsi_close"].loc[idx] > 70:


    def buy_position(self, stock_price):
        if self.budget >= self.quantity*stock_price:
            self.budget = self.budget - self.quantity*stock_price
            self.n_stocks = self.n_stocks+self.quantity
        # else:
        #     sys.exit("No budget available")
    
    def sell_position(self, stock_price):
        if self.n_stocks > 0:
            self.budget = self.budget + self.n_stocks*stock_price
            self.n_stocks = 0

    def change_index(self,data):
        if data.index.name == "time":
            data.reset_index(drop=True, inplace=True)
        return data