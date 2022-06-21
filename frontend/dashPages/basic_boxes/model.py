import numpy as np
import pandas as pd
import plotly.graph_objs as go

def plot_scatter(N=50):
    trace1 = go.Scatter(
        y=np.random.randn(N),
        mode='markers',
        marker=dict(
            size=16,
            color=np.random.randn(N),  # set color equal to a variable
            colorscale='Viridis',
            showscale=True
        )
    )
    return dict(data=[trace1])
