""" Strategies Module"""

class Strategies():
    
    @staticmethod
    def rsi_strategy(rsi_value):
        """
        RSI strategy:
            - When RSI exceeds 70 points we sell position.
            - When RSI drops 30 points we buy position.
        Inputs:
            rsi_value: Current RSI value
        Outputs:             
        """
        if rsi_value > 70:
            return "sell"
        if rsi_value < 30:
            return "buy"
        return None

