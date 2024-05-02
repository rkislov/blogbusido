from fastapi import FastAPI
from core.config import settings
from db.sessions import engine
from db.base_class import Base


def create_table():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_table()
    return app


app = start_application()


@app.get("/")
async def root():
    return {"message": "Hello World"}
