import os
from dash import Dash
import dash_admin_components as dac
import flask
import dash_bootstrap_components as dbc
from dash import dcc, html


def create_dash_app(requests_pathname_prefix: str = None) -> Dash:
    import frontend.dashMain
    from frontend.dashMain.view import navbar, sidebar, body, controlbar, footer

    # =============================================================================
    # Dash App and Flask Server
    # =============================================================================
    # This stylesheet makes the buttons and table pretty.
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app_dash = Dash(
        name=__name__,
        server=flask.Flask(__name__),
        prevent_initial_callbacks=True,
        requests_pathname_prefix=requests_pathname_prefix,

        # routes_pathname_prefix='/dash/',
        assets_folder=os.path.dirname(__file__) + "/frontend"+"/assets"+"/",
        title="BECOM",
        suppress_callback_exceptions=True,
        external_stylesheets=[
            dbc.themes.BOOTSTRAP,
            external_stylesheets,
            # "./asset/css/all.css", #FONT_AWSOME
            # "./asset/css/all.css", # EXTERNAL_STYLESHEETS,
        ],
        meta_tags=[
            {"name": "viewport", "content": "width=device-width, initial-scale=1"}
        ]
    )
    #server = app_dash.server
    app_dash.scripts.config.serve_locally = False
    dcc._js_dist[0]['external_url'] = 'https://cdn.plot.ly/plotly-basic-latest.min.js'

    # =============================================================================
    # App Layout
    # =============================================================================
    app_dash.layout = dac.Page([navbar, sidebar, body, controlbar, footer])

    # =============================================================================
    # Callback
    # =============================================================================
    frontend.dashMain.callbacks.get_callbacks(app_dash)

    # frontend.dashPages.tab_cards.callbacks.get_callbacks(app_dash)
    # frontend.dashPages.basic_boxes.callbacks.get_callbacks(app_dash)

    # frontend.dashPages.gallery_1.callbacks.get_callbacks(app_dash)
    # frontend.dashPages.gallery_2.callbacks.get_callbacks(app_dash)

    return app_dash

# =============================================================================
# Run app
# =============================================================================
# app = create_dash_app()
# if __name__ == '__main__':
#     app.run_server(debug=False)
