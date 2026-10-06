from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.roster import shifts  # noqa: F401

app = FastAPI()


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def home():
    return "<h1>ED Roster</h1>"