import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

MENU_ITEMS = ("basic_cards", "social_cards", "tab_cards",
              "basic_boxes", "value_boxes", 
              "gallery_1", "gallery_2")

def activate(input_id):
    menu_n = len(MENU_ITEMS)
    menu_TF = [False for i in range(menu_n)]
    try:
        menu_idx = MENU_ITEMS.index(input_id.split('_', maxsplit=1)[1])
        menu_TF[menu_idx] = True
    except:
        pass
    return menu_TF
# =============================================================================
# Callbacks
# =============================================================================
def get_callbacks(app_dash):
    # -----------------------------------------------
    # -----------------------------------------------
    @app_dash.callback(
        [Output(f'content_{menu}', 'active')    for menu in MENU_ITEMS],
        [ Input(f'sideMenu_{menu}','n_clicks')  for menu in MENU_ITEMS] )       
    def display_tab(*args):
        ctx = dash.callback_context  # 어떤 Input이 triggered 되었나. 
        if not ctx.triggered:
            raise PreventUpdate
        else:
            input_id = ctx.triggered[0]['prop_id'].split('.')[0]
        return activate(input_id)

    @app_dash.callback(
        [Output(f'sideMenu_{menu}', 'active') for menu in MENU_ITEMS],
        [Input(f'sideMenu_{menu}', 'n_clicks') for menu in MENU_ITEMS])
    def activate_menu(*args):
        ctx = dash.callback_context
        if not ctx.triggered:
            raise PreventUpdate
        else:
            input_id = ctx.triggered[0]['prop_id'].split('.')[0]
        return activate(input_id)

    @app_dash.callback(
        Output('nav_bread', 'text'),
        [Input(f'sideMenu_{menu}', 'n_clicks') for menu in MENU_ITEMS])
    def drop_bread(*args):
        ctx = dash.callback_context
        if not ctx.triggered:
            raise PreventUpdate
        else:
            #input_id = ctx.triggered[0]['prop_id'].split('.')[0]
            input_id = ctx.triggered[0]['prop_id'].split('.')[0].split('_', maxsplit=1)[1]
        return (input_id.replace('_', ' ')).upper()