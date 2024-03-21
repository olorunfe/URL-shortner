from pydantic import BaseModel, AnyHttpUrl


class URLCreate(BaseModel):
    long_url: str
    custom_alias: str = None


class ShortenRequest(BaseModel):
    long_url: AnyHttpUrl

class CustomShortenRequest(BaseModel):
    long_url: AnyHttpUrl
    custom_domain: str
    custom_path: str

class ShortenedURL(BaseModel):
    short_url: str
    long_url: str
