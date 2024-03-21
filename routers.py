# routers.py
from fastapi import APIRouter
from schemas import ShortenRequest, CustomShortenRequest, ShortenedURL
from keygen import generate_short_url
from database import database
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas, models
from database import SessionLocal
import analytics

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

@router.post("/shorten-url")
def shorten_url(url_data: schemas.URLCreate, db: Session = Depends(get_db)):
    # Check if the provided URL already exists in the database
    db_url = crud.get_url_by_long_url(db, url_data.long_url)
    if db_url:
        return {"shortened_url": db_url.shortened_url}

    # If the URL doesn't exist, create a new shortened URL
    short_url = crud.create_short_url(db, url_data)
    return {"shortened_url": short_url.shortened_url}



@router.post("/shorten", response_model=ShortenedURL)
async def shorten_url(request: ShortenRequest):
    short_url = await generate_short_url()
    await database.execute("INSERT INTO shortened_urls (short_url, long_url) VALUES (:short_url, :long_url)", values={"short_url": short_url, "long_url": request.long_url})
    return {"short_url": short_url, "long_url": request.long_url}

@router.post("/custom_shorten", response_model=ShortenedURL)
async def custom_shorten_url(request: CustomShortenRequest):
    short_url = f"https://{request.custom_domain}/{request.custom_path}"
    await database.execute("INSERT INTO shortened_urls (short_url, long_url, custom_domain, custom_path) VALUES (:short_url, :long_url, :custom_domain, :custom_path)", values={"short_url": short_url, "long_url": request.long_url, "custom_domain": request.custom_domain, "custom_path": request.custom_path})
    return {"short_url": short_url, "long_url": request.long_url}



router.mount("/static", StaticFiles(directory="static"), name="static")


@router.get("/", response_class=HTMLResponse)
async def read_main():
    with open("./scissor.html") as file:
        return HTMLResponse(content=file.read(), status_code=200)
    
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas, models
from database import SessionLocal

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/shorten-url")
def shorten_url(url_data: schemas.URLCreate, db: Session = Depends(get_db)):
    # Check if the provided URL already exists in the database
    db_url = crud.get_url_by_long_url(db, url_data.long_url)
    if db_url:
        return {"shortened_url": db_url.shortened_url}

    # If the URL doesn't exist, create a new shortened URL
    short_url = crud.create_short_url(db, url_data)
    return {"shortened_url": short_url.shortened_url}

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas, models
from database import SessionLocal
from analytics import update_analytics, get_analytics

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ... (other routes)

@router.post("/shorten", response_model=schemas.ShortenedURL)
async def shorten_url(request: schemas.ShortenRequest, db: Session = Depends(get_db)):
    short_url = await generate_short_url()
    await database.execute("INSERT INTO shortened_urls (short_url, long_url) VALUES (:short_url, :long_url)",
                           values={"short_url": short_url, "long_url": request.long_url})
    # Update analytics
    update_analytics(db, short_url)
    return {"short_url": short_url, "long_url": request.long_url}

@router.post("/custom_shorten", response_model=schemas.ShortenedURL)
async def custom_shorten_url(request: schemas.CustomShortenRequest, db: Session = Depends(get_db)):
    short_url = f"https://{request.custom_domain}/{request.custom_path}"
    await database.execute("INSERT INTO shortened_urls (short_url, long_url, custom_domain, custom_path) VALUES (:short_url, :long_url, :custom_domain, :custom_path)",
                           values={"short_url": short_url, "long_url": request.long_url, "custom_domain": request.custom_domain, "custom_path": request.custom_path})
    # Update analytics
    update_analytics(db, short_url)
    return {"short_url": short_url, "long_url": request.long_url}

@router.get("/analytics/{short_url}", response_model=dict)
def get_url_analytics(short_url: str, db: Session = Depends(get_db)):
    analytics_data = get_analytics(db, short_url)
    if analytics_data:
        return analytics_data
    else:
        raise HTTPException(status_code=404, detail="Analytics data not found for the provided short URL")