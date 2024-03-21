from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app_config import AppConfig

SQLALCHEMY_DATABASE_URL = "sqlite:///./url_shortener.db"
DATABASE_URL = AppConfig().database_url

# SQLAlchemy Configuration
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

metadata = MetaData()

# Asynchronous Database Configuration
from databases import Database

database = Database(DATABASE_URL)

async def connect_to_database():
    await database.connect()

async def disconnect_from_database():
    await database.disconnect()
