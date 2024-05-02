from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.user import UserCreate
from db.sessions import get_db
from db.repository.user import create_new_user


router = APIRouter()


@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(db, user)
    return user