from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import index, secret, pokemon

# TODO: API Documentation
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/data", StaticFiles(directory="data"), name="data")

app.include_router(index.router)
app.include_router(secret.router)
app.include_router(pokemon.router)
