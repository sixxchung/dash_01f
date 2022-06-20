from dash import dcc, html
import dash_admin_components as dac

from frontend.components.table import make_dash_table
from frontend.components.example_plots import plot_pie, plot_surface, plot_scatter
from ..gallery_1.model import dataframe

dropdown_items = [
    dac.BoxDropdownItem(url="https://www.google.com",
                        children="Link to google"),
    dac.BoxDropdownItem(url="#", children="item 2"),
    dac.BoxDropdownDivider(),
    dac.BoxDropdownItem(url="#", children="item 3")
]

content = dac.TabItem(
    id='content_basic_cards',
    children=[
        html.Div([
            dac.Box([
                dac.BoxHeader(
                    dac.BoxDropdown(dropdown_items),
                    title="Closable box with dropdown",
                    collapsible=True,
                    closable=True,
                ),
                dac.BoxBody(
                    dcc.Graph(
                        figure=plot_pie(),
                        config=dict(
                            displayModeBar=False
                        ),
                        style={'width':'100%'}
                    )
                )
            ],
                color='warning',
                width=6
            ),
            dac.Box([
                dac.BoxHeader(
                    title="Closable box with gradient",
                    collapsible=True,
                    closable=True,
                ),
                dac.BoxBody(
                    dcc.Graph(
                        figure=plot_surface(),
                        config=dict(
                            displayModeBar=False
                        ),
                        style={'width':'100%'}
                    )
                )
            ],
                gradient_color="success",
                width=6
            )
        ],
            className='row'
        ),
        html.Div(
            dac.Box(
                [
                    dac.BoxHeader(
                        collapsible=True,
                        closable=True,
                        title="Card with solidHeader and elevation"
                    ),
                    dac.BoxBody(
                        dcc.Graph(
                            figure=plot_scatter(),
                            config=dict(
                                displayModeBar=False),
                            style={'width':'100%'}
                        )
                    )
                ],
                color='primary',
                solid_header=True,
                elevation=4,
                width=6
            ),
            className='row'
        )
    ],
    active=True
)
