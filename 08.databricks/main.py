import plotly.express as px
from dash import dcc, html, Dash
from dash.dependencies import Input, Output
#from databricks_dash import DatabricksDash
# Load Data
df = px.data.tips()
# Build App
app = Dash(__name__)
server = app.server
app.layout = html.Div([
    html.H1("DatabricksDash Demo"),
    dcc.Graph(id='graph'),
    html.Label([
        "colorscale",
        dcc.Dropdown(
            id='colorscale-dropdown', clearable=False,
            value='plasma', options=[
                {'label': c, 'value': c}
                for c in px.colors.named_colorscales()
            ])
    ]),
])
# Define callback to update graph


@app.callback(
    Output('graph', 'figure'),
    [Input("colorscale-dropdown", "value")]
)
def update_figure(colorscale):
    return px.scatter(
        df, x="total_bill", y="tip", color="size",
        color_continuous_scale=colorscale,
        render_mode="webgl", title="Tips"
    )


if __name__ == "__main__":
    app.run_server(#mode='inline', 
    debug=True)
