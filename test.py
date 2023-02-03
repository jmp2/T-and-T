from Analize_symbol import Analize_symbol
from Calculate_indicator import Calculate_indicator
from simulator import Simulator

############
# Steps:
#   1- Load data
#   2- Compute indicators
#   3- Load strategy
#   4- Perform simulation
#   5- Strategy optimization 

base_path = "data/"
symbol = "AAL"

strategy = "rsi"
budget = 100

if __name__ == "__main__":
    # Load all data
    data = Analize_symbol.create_symbol_dataset(base_path+symbol)
    # Add indicators
    data = Calculate_indicator.compute_rsi(data)
    print(data.head())
    # Perform simulation
    simulator = Simulator(budget, strategy)

    simulator.run_simulation(data)
