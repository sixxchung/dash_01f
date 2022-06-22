import importlib
from dash import html, dcc
import dash_admin_components as dac

from frontend.common.dconsts import MENU_ITEMS


def load_module(module_nm):
    temp = f"frontend.dashPages.{module_nm}.view"
    print(temp)
    rlt = importlib.import_module(temp)
    return rlt
# # basic_cards = load_module('basic_cards')


# =============================================================================
# Dash Admin Components
# =============================================================================
for m in MENU_ITEMS:
    locals()[m] = load_module(m)
    #tmp_menu_content =  [eval(f'{m}.content')]

tmp_menu_content = [eval(f'{m}.content') for m in MENU_ITEMS]
body = dac.Body(
    dac.TabItems(tmp_menu_content),

)

# ---------- Sidebar
subitems = [
    dac.SidebarMenuSubItem(id='sideMenu_gallery_1',
                           label='Gallery 1', icon='arrow-circle-right',
                           badge_label='Soon', badge_color='success'),
    dac.SidebarMenuSubItem(id='sideMenu_gallery_2',
                           label='Gallery 2', icon='arrow-circle-right',
                           badge_label='Soon', badge_color='success')
]

sidebar = dac.Sidebar(
    dac.SidebarMenu(
        children=[
            dac.SidebarMenuItem(id='sideMenu_home',
                                label='HOME', icon='box'),
            dac.SidebarHeader(
                children="Cards"),  # ------------------------------
            dac.SidebarMenuItem(id='sideMenu_stock',
                                label='Stock', icon='box'),
            dac.SidebarMenuItem(id='sideMenu_ivalidation',
                                label='Initial Validation', icon='tachometer-alt'),
        ]
    ),
    title='BECOM',
    skin="dark",  # dark, light
    brand_color="primary",  # primary, secondary, success, info, warning, danger
    color="primary",
    url="https://dash.plotly.com/dash-core-components",
    # "https://adminlte.io/themes/AdminLTE/dist/img/user2-160x160.jpg",
    src="assets/user-01.jpg",
    elevation=4,
    opacity=0.8
)

# ---------- Footer
footer = dac.Footer(
    html.A("@onesixx, BECOM",
           href="https://docs-dash-admin-components.herokuapp.com/l/components",
           target="_blank",
           ),
    right_text="Version 0.6.1"
)

# ---------- Navbar
top_right_ui = dac.NavbarDropdown(
    badge_label="!",
    badge_color="danger",
    header_text="2 Items",
    children=[
        dac.NavbarDropdownItem(
            children="message 1",
            date="today"
        ),
        dac.NavbarDropdownItem(
            children="message 2",
            date="yesterday"
        ),
    ],
    src="https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/explorer/",
)

navbar = dac.Navbar(
    id="nav_bread",
    color="white",
    text="welcome!",  # os.environ.get("WELCOME"),
    fixed=True,
    children=top_right_ui
)

# ---------- Controlbar
controlbar = dac.Controlbar(
    children=[
        html.Br(),
        html.P("Slide to change graph in Basic Boxes"),
        dcc.Slider(
            id='controlbar-slider',
            min=10, max=50, step=1, value=20
        )
    ],
    title="My right sidebar",
    skin="light"
)
