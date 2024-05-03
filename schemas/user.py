from typing import Optional
from uuid import uuid4, UUID

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class ShowUser(BaseModel):
    id: UUID=uuid4()
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_active: bool

    class Config:
        orm_mode = True