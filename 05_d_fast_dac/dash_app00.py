from dash import Dash
import dash_admin_components as dac

import frontend.dashMain
from frontend.dashMain.view import navbar, sidebar, body, controlbar, footer

# =============================================================================
# Dash App and Flask Server
# =============================================================================
app_dash = Dash(__name__)
server = app_dash.server

# =============================================================================
# App Layout
# =============================================================================
app_dash.layout = dac.Page([navbar, sidebar, body, controlbar, footer])

# =============================================================================
# Callback
# =============================================================================
frontend.dashMain.callbacks.get_callbacks(app_dash)

frontend.dashPages.tab_cards.callbacks.get_callbacks(app_dash)
frontend.dashPages.basic_boxes.callbacks.get_callbacks(app_dash)

frontend.dashPages.gallery_1.callbacks.get_callbacks(app_dash)
frontend.dashPages.gallery_2.callbacks.get_callbacks(app_dash)

# =============================================================================
# Run app
# =============================================================================
if __name__ == '__main__':
    app_dash.run_server(debug=False)
