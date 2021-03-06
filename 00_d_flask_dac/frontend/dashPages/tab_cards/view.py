from dash import html
import dash_admin_components as dac

content = dac.TabItem(id='content_tab_cards',
                      children=[
                          html.Div([
                              dac.TabBox(
                                  [
                                      dac.TabBoxHeader(
                                          dac.TabBoxMenu(id='tab_box_1_menu',
                                                         children=[
                                                             dac.TabBoxMenuItem(
                                                                 tab_id='tab_box_1_tab1', label='Tab 01'),
                                                             dac.TabBoxMenuItem(
                                                                 tab_id='tab_box_1_tab2', label='Tab 02'),
                                                             dac.TabBoxMenuItem(
                                                                 tab_id='tab_box_1_tab3', label='Tab 03')
                                                         ]
                                                         ),
                                          collapsible=False,
                                          closable=True,
                                          title="A card with tabs"
                                      ),
                                      dac.TabBoxBody(id='tab_box_1')
                                  ],
                                  width=6,
                                  elevation=2
                              ),
                              dac.TabBox(
                                  [
                                      dac.TabBoxHeader(
                                          dac.TabBoxMenu(
                                              children=[
                                                  dac.TabBoxMenuItem(
                                                      tab_id='tab_box_2_tab1', label='Tab 11', color='dark'),
                                                  dac.TabBoxMenuItem(
                                                      tab_id='tab_box_2_tab2', label='Tab 22', color='danger'),
                                                  dac.TabBoxMenuItem(
                                                      tab_id='tab_box_2_tab3', label='Tab 33', color='primary')
                                              ], id='tab_box_2_menu'),
                                          closable=True,
                                          title="A card with colorful tabs"
                                      ),
                                      dac.TabBoxBody(
                                          id='tab_box_2'
                                      )
                                  ],
                                  color='warning',
                                  width=6,
                                  elevation=2
                              )
                          ], className='row')
                      ]
                      )
