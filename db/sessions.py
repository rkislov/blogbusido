from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

SQLALCHEMY_DATABASE_URL = settings.POSTGRES_URL
print(SQLALCHEMY_DATABASE_URL)
engine = create_engine(f'{SQLALCHEMY_DATABASE_URL}', pool_pre_ping=True)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

