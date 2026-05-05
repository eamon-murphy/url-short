from fastapi import FastAPI

from . import schemas

app = FastAPI()


@app.get("/")
def root():
    return "url-short"


@app.post("/shorten")
def create_url(url: schemas.URLBase):
    return {"short_url": "generated-link"}
