from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from settings import Settings

# The database url comes from a .env file. It follows the structure:
# 'postgresql+psycopg://user:pass@localhost:5432/db_name'
engine = create_engine(Settings().DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
