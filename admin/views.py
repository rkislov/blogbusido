from sqladmin import ModelView
from db.base import Base
from db.models.file import File
from db.models.blog import Blog
from db.models.user import User


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email]
    column_details_exclude_list = [User.password]
    can_delete = False
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"


class FileAdmin(ModelView, model=File):
    column_list = [File.id, File.name]
    name = "Файл"
    name_plural = "Файлы"


class BlogAdmin(ModelView, model=Blog):
    column_list = [Blog.id, Blog.title]
    name = "Запись"
    name_plural = "Записи"
