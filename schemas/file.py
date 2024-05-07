from datetime import datetime
from typing import Optional
from schemas.user import ShowUser
from fastapi import UploadFile, File
from pydantic import BaseModel


class CreateFile(BaseModel):
    blog_id: int


class ShowFile(BaseModel):
    id: int
    name: str
    author: ShowUser
    created_at: datetime
