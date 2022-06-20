import dash_bootstrap_components as dbc
from dash import dcc, html
import dash_admin_components as dac

from .model import dataframe
from frontend.components.table import make_dash_table

controls = dbc.Card(
    body=True,
    children=[
        # dbc.FormGroup(
        dbc.Row([
            dbc.Label("X variable"),
            dcc.Dropdown(
                id="x-variable",
                options=[{"label": col, "value": col} for col in dataframe().columns],
                value="sepal length(cm)",
                style={'width': '100%'}
            ),
        ]),
        
        # dbc.FormGroup(
        dbc.Row([
            dbc.Label("Y variable"),
            dcc.Dropdown(
                id="y-variable",
                options=[{"label": col, "value": col} for col in dataframe().columns],
                value="sepal width(cm)",
                style={'width': '100%'}
            ),
        ]),

        # dbc.FormGroup(
        dbc.Row([
            dbc.Label("Cluster count"),
            dbc.Input(
                id="cluster-count", 
                type="number", 
                value=3
            ),
        ]),
    ]
)

content = dac.TabItem(
    id='content_gallery_1',
    children=[
        html.H1("Iris k-means clustering"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(controls, md=4),
                dbc.Col(dcc.Graph(id="cluster-graph"), md=8),
            ],
            align="center",
        ),
        html.Hr(),
        dbc.Row(
            dbc.Col(
                make_dash_table(dataframe()),
                width={"size": 9, "offset": 1}
            ),
            align="center",
        )
    ],
)
