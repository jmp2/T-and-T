from analize_symbol import Analize_symbol
from simulator import Simulator
from strategies import rsi_macd

############
# Steps:
#   1- Load data
#   2- Compute indicators
#   3- Load strategy
#   4- Perform simulation
#   5- Strategy optimization 


symbol = "AAL"


budget = 10000

if __name__ == "__main__":
    # Load all data
    data = Analize_symbol.create_symbol_dataset(symbol)
    strategy = rsi_macd(value_buy=20, value_sell=70, period_rsi = 14, period_mean_rsi=5, fast_macd = 8, slow_macd = 18, take_profit = 0.01, stop_loss = -0.01)
    strategy.calculate_indicators(data)
    
    date_ini = "25-01-2021"
    date_end = "1-02-2021"

    # Analize_symbol.represent_symbol(data, ["close","rsi_close", 'mean_rsi_close', "macd_close", "macdh_close", "macds_close"],[1,2,2,3,3,3], date_ini = date_ini, date_end = date_end)


    # Perform simulation
    simulator = Simulator(budget, strategy, quantity = 500, fixed_comission=1, variable_comission=0, min_tax=1)

    simulator.run_simulation(data, date_ini = date_ini, date_end = date_end)
