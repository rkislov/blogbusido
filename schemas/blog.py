from typing import Optional
from pydantic import BaseModel, root_validator
from datetime import date
from slugify import slugify
from uuid import uuid4, UUID


class CreateBlog(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None

    @root_validator(pre=True)
    def validate_slug(cls, values):
        if 'title' in values:
            values['slug'] = slugify(values.get('title'))
        return values


class ShowBlog(BaseModel):
    id: str
    title: str
    content: Optional[str]
    created_at: date

    class Config:
        orm_mode = True


class UpdateBlog(CreateBlog):
    pass
