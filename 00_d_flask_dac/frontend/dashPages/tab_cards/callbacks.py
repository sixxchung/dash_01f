from dash.dependencies import Input, Output, State
from . import model

def get_callbacks(app_dash):
    @app_dash.callback(
        Output('tab_box_1', 'children'),
        [Input('tab_box_1_menu', 'active_tab')])
    def display_tabbox1(active_tab):
        # Depending on tab which triggered a callback, show/hide contents of app
        if active_tab == 'tab_box_1_tab1':
            return model.text_1
        elif active_tab == 'tab_box_1_tab2':
            return model.text_2
        elif active_tab == 'tab_box_1_tab3':
            return model.text_3

    @app_dash.callback(
        Output('tab_box_2', 'children'),
        [Input('tab_box_2_menu', 'active_tab')])
    def display_tabbox2(active_tab):
        # Depending on tab which triggered a callback, show/hide contents of app
        if active_tab == 'tab_box_2_tab1':
            return model.text_1
        elif active_tab == 'tab_box_2_tab2':
            return model.text_2
        elif active_tab == 'tab_box_2_tab3':
            return model.text_3
    