from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from database import Base

class ShortenedURL(Base):
    __tablename__ = "shortened_urls"

    id = Column(Integer, primary_key=True, index=True)
    short_url = Column(String, index=True, unique=True)
    long_url = Column(String)
    custom_domain = Column(String, nullable=True)  # Add this line
    custom_path = Column(String, nullable=True)  # Add this line
    analytics = relationship("Analytics", back_populates="shortened_url")

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    long_url = Column(String, index=True)
    shortened_url = Column(String, index=True, unique=True)
    custom_alias = Column(String, index=True, unique=True)

class Analytics(Base):
    __tablename__ = "analytics"

    id = Column(Integer, primary_key=True, index=True)
    short_url_id = Column(Integer, ForeignKey("shortened_urls.id"))
    total_clicks = Column(Integer, default=0)
    referral_sources = Column(String, default="")
    created_at = Column(DateTime, server_default=func.now())

    shortened_url = relationship("ShortenedURL", back_populates="analytics")