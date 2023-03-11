""" Simulator module"""
import sys
from datetime import datetime as dt
import time
from src.report import Report
from src.graphic_report import GraphicReport
from utils.position import Position

class Simulator():

    def __init__(self, budget, strategy, quantity=5, fixed_comission=0, variable_comission=0.01, min_tax=4) -> None:
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
            msg = "\n"+"#"*100 + f"\n\nERROR: Variable comission must be set as a number not percentage.\nPlease, try {variable_comission/100} instead" 
            exit(msg)
        self.variable_comission = variable_comission
        self.min_tax = min_tax
        self.total_comissions = 0
        self.operations_counter = 0
        self.historic_position_list = []
        self.open_position_list = []

        self.report = Report(save_report=True)
        self.graphic_report = GraphicReport()
        self.log_initial_parameters()
    
    def log_initial_parameters(self):
        self.report.register_initial_budget(self.budget)
        self.report.register_strategy(self.strategy)
        self.report.register_taxes(self.fixed_comission, self.variable_comission, self.min_tax)
    
    def close_positions(self, close_date, close_price):
        for position in self.open_position_list:
            if "Symbol" in position.ID:
                position.close_position(close_date, close_price)
                self.historic_position_list.append(position)
                self.open_position_list.remove(position)

    def run_simulation(self, data, date_ini, date_end):
        format = "%d-%m-%Y"
        start_time = dt.strptime(date_ini, format)
        final_time = dt.strptime(date_end, format)
        data = data[data["unix"]>=time.mktime(start_time.timetuple())]
        data = data[data["unix"]<=time.mktime(final_time.timetuple())]

        # Reporting periods
        self.report.register_simulation_period(start_time,final_time)

        data = self.change_index(data)
        for idx in range(data.shape[0]):
            order = self.strategy.perform(data.loc[idx])         
            if order == "buy":
                # self.historic_position_list.append(new_pos)
                buy_flag = self.buy_position(data["close"].loc[idx])
                if buy_flag ==True:
                    new_pos = Position(data.index[idx], data["close"].loc[idx], self.quantity)
                    self.open_position_list.append(new_pos)
                #print(f"\n\n RSI: {data['rsi_close'].loc[idx]} || Order: {order} || Price: {data.close.loc[idx]} || N_Stocks: {self.n_stocks} || Budget: {self.budget}")
            if order == "sell":
                sell_flag = self.sell_position(data["close"].loc[idx])
                if sell_flag == True:
                    self.close_positions(data.index[idx],data["close"].loc[idx])
                #print(f"\n\n RSI: {data['rsi_close'].loc[idx]} || Order: {order} || Price: {data.close.loc[idx]} || N_Stocks: {self.n_stocks} || Budget: {self.budget}")
            # if data["rsi_close"].loc[idx] < 20 or data["rsi_close"].loc[idx] > 70:

        self.report.register_final_budget(self.budget+self.n_stocks*float(data.tail(1)["close"].values))
        self.report.register_total_comissions(self.total_comissions)
        self.report.compute_positions_metrics(self.historic_position_list)
        self.report.print_report()

        self.graphic_report.set_data(data)
        self.graphic_report.register_position_metrics(self.historic_position_list)
        self.graphic_report.plot_graph(self.strategy.get_columns())

    def buy_position(self, stock_price):
        taxes = self.compute_total_taxes("buy", stock_price)
        self.total_comissions += taxes
        if self.budget >= self.quantity*stock_price + taxes:
            self.budget = self.budget - self.quantity*stock_price - taxes
            self.n_stocks = self.n_stocks+self.quantity
            self.strategy.position = stock_price; ###  - -------> HAY QUE AÑADIR QUE SE VAYA CALCULANDO, VER COMO HACERLO CON MÚLTIPLES POSICIONES
            print(f"\n\n Order: buy || Price: {stock_price} || N_Stocks: {self.n_stocks} || Budget: {self.budget}")
            return True
        return False
    
    def sell_position(self, stock_price):
        if self.n_stocks > 0:
            taxes = self.compute_total_taxes("sell",stock_price)
            self.total_comissions += taxes
            self.budget = self.budget + self.n_stocks*stock_price - taxes
            self.n_stocks = 0
            print(f"\n\n Order: sell || Price: {stock_price} || N_Stocks: {self.n_stocks} || Budget: {self.budget}")
            return True
        return False

    def change_index(self,data):
        if data.index.name == "time":
            data.reset_index(drop=True, inplace=True)
        return data
    
    def compute_total_taxes(self, order, stock_price):
        if order=="buy":
            total = self.quantity * stock_price * self.variable_comission + self.fixed_comission
        
        if order == "sell":
            total = self.n_stocks*stock_price*self.variable_comission + self.fixed_comission
        
        if total < self.min_tax:
            total = self.min_tax
        
        return total
        
