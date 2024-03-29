from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import core, users

router = APIRouter()

templates = Jinja2Templates(directory="static/templates")


@router.get("/")
def read_root(request: Request, db: Session = Depends(core.get_db)) -> HTMLResponse:
    active_users, pokemons, names, urls = users.get_active_users(db), [], [], []
    if active_users:
        for active_user in active_users:
            pokemons.append(active_user.pokemon)
            names.append(active_user.name)
            urls.append(active_user.url)
    return templates.TemplateResponse(
        name="index.html",
        request=request,
        context={
            "secret_url": "/api/v1/secret",
            "count": users.get_active_number_of_users(db),
            "pokemons": pokemons,
            "names": names,
            "urls": urls,
        },
    )
