""" Strategies Module"""


from calculate_indicator import Calculate_indicator


class rsi():
    
    def __init__(self, value_buy=30, value_sell=70, period_rsi = 14):
        self.value_buy = value_buy
        self.value_sell = value_sell
        self.period_rsi = period_rsi
        self.position = []

    def get_name(self):
        return "RSI"
    
    def get_columns(self):
        cols = [
            "rsi_close"
        ]
        return cols

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
    
    def calculate_indicators(self, data):
        # Add indicators
        data = Calculate_indicator.compute_rsi(data, self.period_rsi)


class rsi_macd():
    
    def __init__(self, value_buy=30, value_sell=70, period_rsi = 14, period_mean_rsi=5, fast_macd = 8, slow_macd = 18, take_profit = 0.01, stop_loss = -0.01):
        self.value_buy = value_buy
        self.value_sell = value_sell
        self.period_rsi = period_rsi
        self.period_mean_rsi = period_mean_rsi
        self.fast_macd = fast_macd
        self.slow_macd = slow_macd
        self.take_profit = take_profit
        self.stop_loss = stop_loss
        self.position = []
    
    def get_name(self):
        return "RSI_MACD"
    
    def get_columns(self):
        cols = [
            "cross_macd",
            "rsi_close",
            "mean_rsi_close"
        ]
        return cols

    def perform(self, data):
        """
        RSI MACD strategy:
            - When macd offer buy signal and RSI is rising (> than its mean x periods)
            - When stop loss or take profit, we sell.
        Inputs:
            rsi_value: Current RSI value
        Outputs:             
        """
        if data["cross_macd"] == 1 and data["rsi_close"]>data["mean_rsi_close"]:
            return "buy"
        profit = data["close"]/self.position -1
        if profit>self.take_profit or profit<self.stop_loss:
            return "sell"
        return None
    
    def calculate_indicators(self, data):
        # Add indicators
        data = Calculate_indicator.compute_rsi(data, self.period_rsi)
        data = Calculate_indicator.compute_macd(data, self.fast_macd, self.slow_macd)
        data = Calculate_indicator.compute_mean_rsi(data, self.period_mean_rsi)