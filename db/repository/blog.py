from sqlalchemy.orm import Session
from schemas.blog import CreateBlog, UpdateBlog
from db.models.blog import Blog


def create_new_blog(db: Session, blog: CreateBlog, file, author_id: int) -> Blog:
    blog = Blog(
        title=blog.title,
        slug=blog.slug,
        content=blog.content,
        author_id=author_id,
        )
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def retrieve_blog(db: Session, blog_id: int) -> Blog:
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    return blog


def list_blogs(db: Session) -> list[Blog]:
    blogs = db.query(Blog).filter(Blog.is_active == True).all()
    return blogs


def update_blog(id:int, blog: UpdateBlog, author_id: int, db: Session):
    blog_in_db = db.query(Blog).filter(Blog.id == id).first()
    if not blog_in_db:
        return {"error": f"Запись с ID {id} не существует"}
    if blog_in_db.author_id != author_id:
        return {"error": f"У вас нет прав на редактирование записи ID {blog_in_db.id}"}
    blog_in_db.title = blog.title
    blog_in_db.content = blog.content
    db.add(blog_in_db)
    db.commit()
    return blog_in_db


def delete_blog(id: int, author_id: int, db: Session):
    blog_in_db = db.query(Blog).filter(Blog.id == id)
    if not blog_in_db.first():
        return {"error":f"записи с id {id} не существует"}
    if blog_in_db.first().author_id != author_id:
        return {"error": f"У вас нет прав на удаление записи ID {id}"}
    blog_in_db.delete()
    db.commit()
    return {"msg":f"deleted blog with id {id}"}
