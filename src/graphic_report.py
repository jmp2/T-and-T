import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

pio.renderers.default='browser'

class GraphicReport():

    def __init__(self) -> None:
        self.data = None
        self.position_list = None
        self.price = []
        self.current_budget = []

    def append_record(self, price, position):
        self.price.append(price)
        self.current_budget.append(position)

    def compute_comparison(self):
        df_comp = pd.DataFrame()
        df_comp["price"] = self.price / self.price[0]
        df_comp["position"] = self.current_budget / self.current_budget[0]
        return df_comp

    def set_data(self, data):
        self.data = data

    def register_position_metrics(self, position_list):
        self.position_list = position_list

    def plot_graph(self, cols, plotly=False):
        if plotly == True:
            self.plotly_plot(cols)
        else:
            self.seaborn_plot(cols)

    def plotly_plot(self, cols):
        # fig = make_subplots(rows=nplots, cols=1)
        fig = make_subplots(rows=2, cols=1)
        fig.add_trace(go.Scatter(x=self.data.index, y=self.data["close"], name="Price"), row=1, col=1)
        for pos in self.position_list:
            fig.add_vline(x=pos.open_date, line_width=1, line_color="green")
            fig.add_vline(x=pos.close_date, line_width=1, line_color="red")
        for column in cols:
            fig.add_trace(go.Scatter(x=self.data.index, y=self.data[column], name=column), row=2, col=1)
        fig.show()

    def seaborn_plot(self, cols):
        _, axes = plt.subplots(3, 1, figsize=(18, 10))
        g = sns.lineplot(ax=axes[0], data=self.data, x=self.data.index, y="close")
        for pos in self.position_list:
            g.axvline(x=pos.open_date, color="green")
            g.axvline(x=pos.close_date, color="red")
        for col in cols:
            sns.lineplot(ax=axes[1], data=self.data,
                         x=self.data.index,
                         y=col, label=col)
        df_comp = self.compute_comparison()
        sns.lineplot(ax=axes[2], data=df_comp, x=self.data.index,
                     y="price", label="Index returns")
        sns.lineplot(ax=axes[2], data=df_comp, x=self.data.index,
                     y="position", label="Strategy returns")
        plt.legend()
        plt.show()
