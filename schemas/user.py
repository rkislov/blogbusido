from pydantic import BaseModel, EmailStr, Field



class UserCreate(BaseModel):
    email: EmailStr
    password: str