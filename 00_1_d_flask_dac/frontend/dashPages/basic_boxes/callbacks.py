import plotly.graph_objs as go
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output, State

from .model import plot_scatter

def get_callbacks(app_dash):
    # Update figure on slider change
    @app_dash.callback(
        Output('box-graph', 'figure'),
        [Input('controlbar-slider', 'value')])
    def update_box_graph(value):
        # go.Figure()
        return plot_scatter(value)
