from datetime import datetime

from pydantic import BaseModel, HttpUrl


class URLCreate(BaseModel):
    url: HttpUrl


class URLResponse(BaseModel):
    id: str
    url: HttpUrl
    short_code: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class URLStatsResponse(URLResponse):
    access_count: int
