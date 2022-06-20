import dash_bootstrap_components as dbc
from dash import dcc, html
import dash_admin_components as dac

#from pages.home.model import dataframe

content = dac.TabItem(id='content_home',
                      children=[
                          html.P(
                              'home sweet home'
                          )
                      ],

                      )
