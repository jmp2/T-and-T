import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

import matplotlib.pyplot as plt
import seaborn as sns

pio.renderers.default='browser'

class GraphicReport():

    def __init__(self) -> None:
        self.data = None
        self.position_list = None

    def set_data(self, data):
        self.data = data

    def register_position_metrics(self, position_list):
        self.position_list = position_list
    
    def plot_graph(self, cols, col_pos, plotly=False):
        if plotly == True:
            self.plotly_plot(cols)
        else:
            self.seaborn_plot(cols, col_pos)

    
    def plotly_plot(self, cols):
        fig = make_subplots(rows=len(cols), cols=1)
        #fig = make_subplots(rows=2, cols=1)
        fig.add_trace(go.Scatter(x=self.data.index, y=self.data["close"], name="Price"), row=1, col=1)
        for pos in self.position_list:
            fig.add_vline(x=pos.open_date, line_width=1, line_color="green")
            fig.add_vline(x=pos.close_date, line_width=1, line_color="red")
        for column in cols:
            fig.add_trace(go.Scatter(x=self.data.index, y=self.data[column], name=column), row=2, col=1)
        fig.show()
    
    def seaborn_plot(self, cols, col_pos):
        print(col_pos)
        fig, axes = plt.subplots(max(col_pos)+1, 1, figsize=(18, 10))
        for ax in axes:
            ax.grid()
        g = sns.lineplot(ax=axes[0], data=self.data, x=self.data.index, y="close")

        for pos in self.position_list:
            g.axvline(x=pos.open_date, color="green")
            g.axvline(x=pos.close_date, color="red")
        
        for i in range(len(cols)):
            sns.lineplot(ax=axes[col_pos[i]], data=self.data, x=self.data.index, y=cols[i])

        plt.show()