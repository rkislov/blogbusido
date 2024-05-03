from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.sessions import get_db
from schemas.blog import ShowBlog, CreateBlog
from db.repository.blog import create_new_blog


router = APIRouter()


@router.post('/', response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
async def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    blog = create_new_blog(db, blog)
    return blog