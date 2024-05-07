from fastapi import FastAPI

from admin.views import UserAdmin, FileAdmin, BlogAdmin
from core.config import settings
from db.sessions import engine
from db.base import Base
from apis.base import api_router
from sqladmin import Admin, ModelView
from  admin.auth import authentication_backend


def include_router(app):
    app.include_router(api_router)


def create_table():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_table()
    include_router(app)
    return app


app = start_application()
admin = Admin(app, engine, authentication_backend=authentication_backend)


admin.add_view(UserAdmin)
admin.add_view(FileAdmin)
admin.add_view(BlogAdmin)




@app.get("/")
async def root():
    return {"message": "Hello World"}
