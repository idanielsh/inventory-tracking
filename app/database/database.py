import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

connection_string = os.getenv("DATABASE_URL").replace('postgres', 'postgresql')
engine = create_engine(
    connection_string
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base(bind=engine)
DatabaseSession = get_database