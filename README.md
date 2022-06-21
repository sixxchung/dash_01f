# dash_01f

## ADD NEW MENU (sixx)
1. frontend/common/consts.py
1. add frontend/dataMain/view
1. add frontend/dashPages/sixx
1. add frontend/dashPages/sixx/view
```python
content = dac.TabItem(
    id='content_sixx',
```
## dcc (dash-core-components)
https://dash.plotly.com/dash-core-components


## dbc  (bootstrap)
https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/explorer/

## dac (dash_admin_components)
https://docs-dash-admin-components.herokuapp.com/
https://docs-dash-admin-components.herokuapp.com/l/components

navbar, sidebar, collapsible boxes, boxes with tab, etc.
compatible with dbc
Cons:
uses AdminLTE3 jQuery for sliding and resizing page, but in React manner.
the Bootstrap 4 css is preloaded (just like in shinydashboard), thus usage of different Bootstrap templates is restricted.
