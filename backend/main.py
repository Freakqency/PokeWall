from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()

app.mount("/static", StaticFiles(directory="backend/static"), name="static")

templates = Jinja2Templates(directory="backend/static/templates")


@app.get("/")
def root(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(name="index.html", request=request)
