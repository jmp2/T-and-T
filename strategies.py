""" Strategies Module"""

class rsi():
    
    def __init__(self, value_buy=30, value_sell=70):
        self.value_buy = value_buy
        self.value_sell = value_sell

    
    def perform(self, data):
        """
        RSI strategy:
            - When RSI exceeds 70 points we sell position.
            - When RSI drops 30 points we buy position.
        Inputs:
            rsi_value: Current RSI value
        Outputs:             
        """
        rsi_value = data["rsi_close"]
        if rsi_value > self.value_sell:
            return "sell"
        if rsi_value < self.value_buy:
            return "buy"
        return None


class rsi_macd():
    
    
    def perform(rsi_value, value_buy, value_sell):
        """
        RSI strategy:
            - When RSI exceeds 70 points we sell position.
            - When RSI drops 30 points we buy position.
        Inputs:
            rsi_value: Current RSI value
        Outputs:             
        """
        if rsi_value > value_sell:
            return "sell"
        if rsi_value < value_buy:
            return "buy"
        return None