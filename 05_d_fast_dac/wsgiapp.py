from re import I
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.responses import RedirectResponse

from dashapp import create_dash_app

urlPath_dash = '/dash'
port_dash = 8050

app_fastapi = FastAPI()
app_fastapi.router.redirect_slashes = False

app_dash = create_dash_app(requests_pathname_prefix=urlPath_dash)
app_fastapi.mount(urlPath_dash, WSGIMiddleware(app_dash.server))


@app_fastapi.get("/")
def redirect_root():
    url = "http://0.0.0.0:" + str(port_dash) + urlPath_dash
    response = RedirectResponse(url)
    return response

# @app_fastapi.get("/")
# def read_main():
#     return {
#         "routes": [
#             {"method": "GET", "path": "/", "summary": "Landing"},
#             {"method": "GET", "path": "/status", "summary": "App status"},
#             {"method": "GET", "path": "/dash",
#                 "summary": "Sub-mounted Dash application"},
#         ]
#     }


@app_fastapi.get("/status")
def get_status():
    return {"status": "ok"}
