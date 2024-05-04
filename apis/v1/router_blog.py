from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from db.sessions import get_db
from schemas.blog import ShowBlog, CreateBlog, UpdateBlog
from db.repository.blog import create_new_blog, retrieve_blog, list_blogs, update_blog, delete_blog
from db.models.user import User
from apis.v1.router_login import  get_current_user


router = APIRouter()


@router.post('/blog', response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
async def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    blog = create_new_blog(db, blog, author_id=get_current_user.id)
    return blog


@router.get('/blog/{blog_id}', response_model=ShowBlog, status_code=status.HTTP_200_OK)
async def get_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = retrieve_blog(db, blog_id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Запись с id {id} не найдена')
    return blog


@router.get('/blogs', response_model=List[ShowBlog])
async def get_blogs(db: Session = Depends(get_db)):
    blogs = list_blogs(db)
    return blogs


@router.put("/blog/{id}", response_model=ShowBlog)
def update_a_blog(id:int, blog: UpdateBlog, db:Session = Depends(get_db)):
    blog = update_blog(id=id, blog=blog, author_id=get_current_user.id, db=db)
    if not blog:
        raise HTTPException(detail=f"Blog with id {id} does not exist")
    return blog


@router.delete("/delete/{id}")
def delete_a_blog(id: int, db: Session = Depends(get_db), current_user: User=Depends(get_current_user)):
    message = delete_blog(id=id, author_id=current_user.id, db=db)
    if message.get("error"):
        raise HTTPException(
            detail=message.get("error"), status_code=status.HTTP_400_BAD_REQUEST
        )
    return {"msg": f"Successfully deleted blog with id {id}"}
