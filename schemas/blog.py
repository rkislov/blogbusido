from typing import Optional
from pydantic import BaseModel, model_validator
from datetime import datetime
from slugify import slugify
from schemas.user import ShowUser
from schemas.file import ShowFile, CreateFile


class CreateBlog(BaseModel):
    title: str
    slug: Optional[str] = None
    content: Optional[str] = None

    @model_validator(mode='before')
    def validate_slug(cls, values):
        if 'title' in values:
            values['slug'] = slugify(values.get('title'))
        return values


class ShowBlog(BaseModel):
    id: int
    title: str
    content: Optional[str]
    created_at: datetime
    author: ShowUser
    files: list[ShowFile]

    class Config:
        orm_mode = True


class UpdateBlog(CreateBlog):
    pass
