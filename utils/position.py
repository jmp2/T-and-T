"""
Position class to differentiate operations
"""
class Position():
    def __init__(self, open_date, open_price, quantity,symbol="Symbol") -> None:
        self.ID = str(symbol)+"_"+str(open_date)
        self.open_date = open_date
        self.open_price = open_price
        self.quantity = quantity
        self.close_date = None
        self.close_price = None

    def close_position(self, close_date, close_price):
        self.close_date = close_date
        self.close_price = close_price