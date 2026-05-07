import uuid
from datetime import datetime

from fastapi import FastAPI, status

from . import schemas

app = FastAPI()


@app.get("/")
def root():
    return "url-short"


@app.post(
    "/shorten",
    response_model=schemas.URLResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"description": "Validation errors..."},
    },
)
def create_url(url: schemas.URLCreate):
    pass


@app.get(
    "/shorten/{short_code}",
    response_model=schemas.URLResponse,
    status_code=status.HTTP_200_OK,
    responses={
        404: {"description": "Short code does not exist"},
    },
)
def retrieve_url(short_code: str):
    pass


@app.put(
    "/shorten/{short_code}",
    response_model=schemas.URLResponse,
    status_code=status.HTTP_200_OK,
    responses={
        400: {"description": "Validation errors..."},
        404: {"description": "Short code does note exist"},
    },
)
def update(short_code: str):
    pass


@app.delete(
    "/shorten/{short_code}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        404: {"description": "Short code does not exist"},
    },
)
def delete(short_code: str):
    pass


@app.get(
    "/shorten/{short_code}/stats",
    response_model=schemas.URLStatsResponse,
    status_code=status.HTTP_200_OK,
    responses={
        404: {"description": "Short code does not exist"},
    },
)
def get_stats(short_code: str):
    pass
