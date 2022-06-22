from re import I
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.responses import RedirectResponse

from dashapp import create_dash_app
from frontend.common.dconsts import Path_for_dash, Port_for_dash

app_fastapi = FastAPI()
app_fastapi.router.redirect_slashes = False

app_dash = create_dash_app(requests_pathname_prefix=Path_for_dash)
app_fastapi.mount(Path_for_dash, WSGIMiddleware(app_dash.server))


@app_fastapi.get("/")
def redirect_root():
    url = "http://0.0.0.0:" + str(Port_for_dash) + Path_for_dash + "/"
    # print(f"sixx==>{url}")
    response = RedirectResponse(url)
    return response


@app_fastapi.get("/status")
def get_status():
    return {"status": "ok"}
