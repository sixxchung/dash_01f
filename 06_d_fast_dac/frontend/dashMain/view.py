import importlib
from dash import html, dcc
import dash_admin_components as dac
from frontend.common.consts import MENU_ITEMS

def load_module(module_nm):
    rlt = importlib.import_module(f"frontend.dashPages.{module_nm}.view")
    return rlt
# basic_cards = load_module('basic_cards')
for m in MENU_ITEMS:
    locals()[m] = load_module(m)

# =============================================================================
# Dash Admin Components
# =============================================================================
tmp_menu_content = [eval(f'{m}.content') for m in MENU_ITEMS]
body = dac.Body(
    dac.TabItems(tmp_menu_content)
)

# ---------- Sidebar
subitems = [
    dac.SidebarMenuSubItem(id='sideMenu_gallery_1',
                           label='Gallery 1',
                           icon='arrow-circle-right',
                           badge_label='Soon',
                           badge_color='success'),
    dac.SidebarMenuSubItem(id='sideMenu_gallery_2',
                           label='Gallery 2',
                           icon='arrow-circle-right',
                           badge_label='Soon',
                           badge_color='success')
]

sidebar = dac.Sidebar(
    dac.SidebarMenu(
        children=[
            dac.SidebarMenuItem(id='sideMenu_home',
                                label='HOME', icon='box'),
            dac.SidebarHeader(
                children="Cards"),  # ------------------------------
            dac.SidebarMenuItem(id='sideMenu_basic_cards',
                                label='Basic cards', icon='box'),
            dac.SidebarMenuItem(id='sideMenu_social_cards',
                                label='Social cards', icon='id-card'),
            dac.SidebarMenuItem(id='sideMenu_tab_cards',
                                label='Tab cards', icon='image'),
            dac.SidebarHeader(
                children="Boxes"),  # ------------------------------
            dac.SidebarMenuItem(id='sideMenu_basic_boxes',
                                label='Basic boxes', icon='desktop'),
            dac.SidebarMenuItem(id='sideMenu_value_boxes',
                                label='Value/Info boxes', icon='suitcase'),
            dac.SidebarHeader(
                children="Gallery"),  # ----------------------------
            dac.SidebarMenuItem(
                label='Galleries', icon='cubes',
                children=subitems),
        ]
    ),
    title='Dash Admin',
    skin="light",
    color="primary",
    brand_color="primary",
    url="https://quantee.ai",
    src="https://adminlte.io/themes/AdminLTE/dist/img/user2-160x160.jpg",
    elevation=3,
    opacity=0.8
)

# ---------- Footer
footer = dac.Footer(
    html.A("@DawidKopczyk, Quantee",
           href="https://twitter.com/quanteeai",
           target="_blank",
           ),
    right_text="2019"
)

# ---------- Navbar
top_right_ui = dac.NavbarDropdown(
    badge_label="!",
    badge_color="danger",
    src="https://quantee.ai",
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
    ]
)

navbar = dac.Navbar(
    id = "nav_bread",
    color="white",
    text="I can write text in the navbar!",  # os.environ.get("WELCOME"),
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