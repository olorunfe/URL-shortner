from sqlalchemy.orm import Session
import models, schemas

def create_short_url(db: Session, url_data: schemas.URLCreate):
    db_url = models.URL(**url_data.dict())
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_url_by_long_url(db: Session, long_url: str):
    return db.query(models.URL).filter(models.URL.long_url == long_url).first()
