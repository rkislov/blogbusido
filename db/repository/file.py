from sqlalchemy.orm import Session
from schemas.file import ShowFile
from db.models.file import File
from fastapi import UploadFile


def create_file(db: Session, file: UploadFile, author_id: int, blog_id: int) -> File:
    file = File(
        name=file.filename,
        author_id=author_id,
        blog_id=blog_id,
    )
    db.add(file)
    db.commit()
    db.refresh(file)
    return file
