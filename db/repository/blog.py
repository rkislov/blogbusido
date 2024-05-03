from sqlalchemy.orm import Session
from schemas.blog import CreateBlog
from db.models.blog import Blog
import uuid

def create_new_blog(db: Session, blog: CreateBlog, author_id:uuid = 'b8ba6a5c-9dc9-4357-bf36-aeb87d30c4f7') -> Blog:
    blog = Blog(**blog.dict(), author_id=author_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog