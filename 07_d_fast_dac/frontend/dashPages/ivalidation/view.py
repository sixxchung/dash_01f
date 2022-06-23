from dataclasses import asdict
from frontend.common import dconfig, dconsts, dcode
from dash import dcc, html
import dash_admin_components as dac
import dash_bootstrap_components as dbc

from dash import dash_table
from dash.dash_table.Format import Format, Group, Scheme
from dash.dash_table.Format import Group

import pandas as pd
from datetime import date, timedelta, datetime

from frontend.components.server_function import *
from frontend.components.functions import formatter_2_decimals

from . import model


def make_dash_table(df):
    body = []
    header = []

    for column in df.columns:
        header.append(html.Th(column))

    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td(formatter_2_decimals(row[i])))
        body.append(html.Tr(html_row))

    tHead = html.Thead(html.Tr(header))
    tBody = html.Tbody(body)
    table = html.Table([tHead, tBody])

    return table


dataTable_column = pd.DataFrame(
    columns=[
        'Date', 'Bank', 'WeekDay', 'Voltage', 'Current', 'ChargeQ', 'DataCount', 'DataFail', 'UseYN', 'UseDesc'
    ]
)
# pd.DataFrame({
#     'Date'      : [''],
#     'Bank'      : [''],
#     'WeekDay'   : [''],
#     'Voltage'   : [''],
#     'Current'   : [''],
#     'ChargeQ'   : [''],
#     'DataCount' : [''],
#     'DataFail'  : [''],
#     'UseYN'     : [''],
#     'UseDesc'   : ['']
# })
# def df_bank():
#     # assign data of lists.
#     lstBank = list(range(1,4))
#     data = {'name': lstBank, 'code': lstBank}
#       # Create DataFrame
#     df = pd.DataFrame(data)
#     return df

r1_condi_1 = dbc.Card(
    body=True,
    #style={"height": "280px"},
    children=[
        # dbc.FormGroup(
        dbc.Row([
            dbc.Label("Bank:"),
            dcc.Dropdown(
                id="cbo_dash_bank",
                options={v: k for k, v in asdict(dcode.Bank_CD()).items()},
                value="1",
            ),
        ]), html.Br(),
        dbc.Row([
            dbc.Label("Data Type:"),
            dcc.Dropdown(
                id="cbo_dash_data_type",
                options={v: k for k, v in asdict(dcode.DType_CD()).items()},
                value="C",
            )
        ]), html.Br(),
        dbc.Row([
            dbc.Col(
                width=6,  # style={"padding-right": "5px"},
                children=[
                    # dbc.Label("Stand Date"),
                    dbc.Label("From:"),  # id="lbl_date1"),
                    dcc.DatePickerSingle(
                        id='dtp_dash_stand',
                        min_date_allowed=date(2019, 12, 13),
                        max_date_allowed=date.today(),
                        initial_visible_month=date.today(),
                        # date=date.today()-timedelta(days=1),
                        date=datetime.strptime(
                            '2022-01-05', '%Y-%m-%d').date(),
                        display_format='YYYY-MM-DD',
                        style={"font-size": "1rem"}
                    )
                ]
            ),

            dbc.Col(
                width=6,  # style={"align": "right", "padding-left": "5px"},
                children=[
                    dbc.Label("to"),
                    dcc.DatePickerSingle(
                        id='dtp_dash_compare',
                        min_date_allowed=date(2019, 12, 13),
                        max_date_allowed=date.today(),
                        initial_visible_month=date.today(),
                        # date.today()-timedelta(days=1),
                        date=datetime.strptime(
                            '2022-01-06', '%Y-%m-%d').date(),
                        display_format='YYYY-MM-DD',
                        style={"font-size": 8}
                    )
                ],
            )
        ]),
        dbc.Row([
            # [
            # dbc.Col(children=html.Div([
            html.Br(),
            dbc.Button("Load", color="primary",
                       className="me-1", id="dash_btn_load"),
            # dbc.Button(
            #     html.Span(
            #         ["Load", html.I(className="fas fa-arrow-alt-circle-right ml-2")]),
            #     id="dash_btn_load",
            #     color="dark")
            # ],className="d-grid gap-2",) , width=12,),
            # ],style={'padding-top': '5px', 'padding-bottom': '5px'},
        ])
    ]
)

r1_condi_2 = dbc.Card(
    [
        dbc.Row([
            dcc.Loading(id="dash_plot_5_loading", type="default",
                children=dcc.Graph(
                    id="dash_plot_5",
                    figure={
                        'data': [{'y': [0, 0]}],
                        # 'layout': {'height': 230}
                    })
            )
        ]),
    ],
    #style={"height": "280px"},
    body=True,
)

r1_condi_3 = html.Div(
    [
        dbc.Row([
            dac.ValueBox(
                id='dash_box_voltage',
                value="0 V",
                subtitle="Voltage [0%]",
                color="primary", icon="chart-line",
                width=6
            ),
            dac.ValueBox(
                id='dash_box_cq',
                value="0 Ah",
                subtitle="Charge Q [0%]",
                color="info", icon="charging-station",
                width=6
            ),
        ]),
        dbc.Row([
            dac.ValueBox(
                id='dash_box_datacount',
                value="0",
                subtitle="Data Count [0%]",
                color="warning", icon="database",
                width=6
            ),
            dac.ValueBox(
                id='dash_box_current_c',
                value="0 A",
                subtitle="Current(C) [0%]",
                color="success", icon="wave-square",
                width=6
            ),
        ]),
        dbc.Row([
            dac.ValueBox(
                id='dash_box_current_d',
                value="0 A",
                subtitle="Current(D) [0%]",
                color="secondary", icon="wave-square",
                width=6
            ),
            dac.ValueBox(
                id='dash_box_fail',
                value="0",
                subtitle="Data Fail [0%]",
                color="danger", icon="frown",
                width=6
            )
        ]),
    ],
)

# r2_dash_control_1 = dbc.Card(
r2_dash_control_1 = dac.SimpleBox(
    title="Voltage by Rack",
    children=[
        dcc.Loading(
            id="dash_plot_1_loading",
            type="cube",
            children=dcc.Graph(
                id="dash_plot_1",
                config=dict(displayModeBar=False),
            )
        )
    ],
    width=12
)
r2_dash_control_2 = dac.SimpleBox(
    title="Voltage by Rack",
    children=[
        dcc.Loading(
            id="dash_plot_2_loading",
            type="cube",
            children=dcc.Graph(
                id="dash_plot_2",
                config=dict(displayModeBar=False),
            )
        )
    ],
    width=12
)
r3_dash_control_3 = dac.SimpleBox(
    title="Temperature by Rack",
    children=[
        dcc.Loading(
            id="dash_plot_3_loading",
            type="dot",
            children=dcc.Graph(
                id="dash_plot_3",
                config=dict(displayModeBar=False),
                figure={
                    'data': [{'y': [0, 0]}],
                    # 'layout': {'height': 400}
                }
            )
        )
    ],
    width=12
)

r3_dash_control_4 = dac.SimpleBox(
    title="Charge/Discharge Q by Rack",
    children=[
        dcc.Loading(
            id="dash_plot_4_loading",
            type="circle",
            children=dcc.Graph(
                id="dash_plot_4",
                config=dict(displayModeBar=False),
                figure={
                    'data': [{'y': [0, 0]}],
                    # 'layout': {'height': 400}
                }
            )
        )
    ],
    width=12
)

dash_plot_selection_dataview = dbc.Modal(
    [
        # dbc.ModalHeader(dbc.ModalTitle("Train/Test Data")),
        # dbc.ModalBody(
        #     children=[
        #         dbc.Label("Selected Data"),
        #          html.H1(id='dash_selection_DT')
        #     ]),
    ],
    id="dash_modal_selection_data",
    size="xl",
    fullscreen=False,
)

dash_DataTable_1_columns = [
    dict(id='Date', name='Date', type='text'),
    dict(id='Bank', name='Bank', type='text'),
    dict(id='WeekDay', name='WeekDay', type='text'),
    dict(id='Voltage', name='Voltage', type='numeric', format=Format(
        precision=2, scheme=Scheme.fixed).group(True)),
    dict(id='Current', name='Current', type='numeric', format=Format(
        precision=2, scheme=Scheme.fixed).group(True)),
    dict(id='ChargeQ', name='Charge Q', type='numeric',
         format=Format(precision=2, scheme=Scheme.fixed).group(True)),
    dict(id='DataFail', name='Data Fail', type='numeric',
         format=Format(precision=0, scheme=Scheme.fixed).group(True)),
    dict(id='DataCount', name='Data Count', type='numeric',
         format=Format(precision=0, scheme=Scheme.fixed).group(True)),
    dict(id='UseYN', name='Use Y/N', type='text'),
    dict(id='UseDesc', name='Use Desc.', type='text'),
]

dash_DataTable_1 = dash_table.DataTable(
    id='dash_DT',

    columns=dash_DataTable_1_columns,

    style_table={'height': '800px', 'overflowY': 'auto', 'overflowX': 'auto'},
    style_cell={'padding-top': '2px', 'padding-bottom': '2px',
                'padding-left': '5px', 'padding-right': '5px'},

    sort_action='custom',
    sort_mode='multi',
    sort_by=[],

    page_action='native',
    page_current=0,
    page_size=25,

                # fixed_columns={'headers': True, 'data': 1},
                # style_as_list_view=True,


                style_cell_conditional=[
                    {'if': {'column_id': 'Date'},
                        'textAlign': 'center', 'width': '7%'},
                    {'if': {'column_id': 'Bank'},
                        'textAlign': 'center', 'width': '5%'},
                    {'if': {'column_id': 'WeekDay'},
                        'textAlign': 'center', 'width': '7%'},
                    {'if': {'column_id': 'Voltage'},
                        'textAlign': 'right', 'width': '10%'},
                    {'if': {'column_id': 'Current'},
                        'textAlign': 'right', 'width': '10%'},
                    {'if': {'column_id': 'ChargeQ'},
                        'textAlign': 'right', 'width': '10%'},
                    {'if': {'column_id': 'DataFail'},
                        'textAlign': 'right', 'width': '10%'},
                    {'if': {'column_id': 'DataCount'},
                        'textAlign': 'right', 'width': '10%'},
                    {'if': {'column_id': 'UseYN'},
                        'textAlign': 'center', 'width': '6%'},
                    {'if': {'column_id': 'UseDesc'},
                        'textAlign': 'left', 'width': '25%'},
    ],
    # style_data_conditional=[
    #     {
    #         'if': {'row_index': 0}, 'backgroundColor': '#FFF2CC'  ,
    #         # data_bars(dataTable_column, 'ChargeQ')  +
    #         # data_bars(dataTable_column, 'Voltage'),
    #     },
    # ],
    style_header={
                    'backgroundColor': '#626464',
                    'fontWeight': 'bold',
                    'textAlign': 'center',
                    'height': '40px'
    },
    # export_format='xlsx',
    # export_headers='display',
)

content = dac.TabItem(
    id='content_ivalidation',
    children=dbc.Tabs([
        dbc.Tab(
            id='tab1_ivalidation', label="Raw Data",
            active_label_class_name="fw-bold",
            tab_class_name="text-center",  # flex-grow-1
            # children=html.Div(
            children=[
                dcc.Store(id='ds_dash_df',         storage_type='memory'),
                dcc.Store(id='ds_dash_compare_df', storage_type='memory'),
                dcc.Store(id='ds_dash_box_data',   storage_type='memory'),
                dbc.Row(  # 111
                    children=[
                        dbc.Row(html.Br()),
                        # style={"height": "100%"},),
                        dbc.Col(r1_condi_1, md=3, ),
                        # style={"height": "100%"},),
                        dbc.Col(r1_condi_2, md=5, ),
                        # style={"height": "100%"},),
                        dbc.Col(r1_condi_3, md=4, ),
                    ],
                    align="center",
                    # style={"height":"290"},
                ),
                dbc.Row(  # 222
                    children=[
                        dbc.Col(r2_dash_control_1, md=6),
                        dbc.Col(r2_dash_control_2, md=6),
                    ],
                    align="center",
                ),
                dbc.Row(  # 333
                    children=[
                        dbc.Col(r3_dash_control_3, md=6),
                        dbc.Col(r3_dash_control_4, md=6),
                    ],
                    align="center",
                ),
            ]
        ),
        # TAB2 TAB2 TAB2 TAB2 TAB2 TAB2 TAB2 TAB2 TAB2 TAB2 TAB2 TAB2 TAB2 TAB2
        dbc.Tab(
            label='Calendar',
            id='tab2_ivalidation',
            active_label_class_name="fw-bold",
            tab_class_name="text-center",  # flex-grow-1
            children=[
                html.Br(),
                html.Div(
                    children=[
                        dcc.DatePickerRange(
                            id='dash_tab2_date_range',
                            min_date_allowed=date(2019, 12, 13),
                            max_date_allowed=date.today()-timedelta(days=1),
                            initial_visible_month=date.today()-timedelta(days=30),
                            start_date=datetime.strptime(
                                '2020-01-05', '%Y-%m-%d').date(),
                            end_date=date.today()-timedelta(days=1),
                            display_format='YYYY-MM-DD'
                        ),
                        dbc.Button(
                            "Load",
                            id="dash_btn_load_check_data", className="me-2 fas fa-arrow-alt-circle-right",
                            color="dark",
                            style={"margin-left": "15px"}
                        ),
                    ]
                ),
                html.Br(),
                html.Div(
                    children=[
                        dcc.Store(
                            id='dash_store_data_table',
                            storage_type='memory'
                        ),
                        dcc.Loading(
                            id="dash_DT_1_loading",
                            type="default",
                            children=[dash_DataTable_1],
                        )
                    ]
                )
            ]
        )
    ]),
    active=True
)
