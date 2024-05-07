from fastapi import APIRouter, UploadFile, Depends
from schemas.file import ShowFile, CreateFile
from apis.v1.router_login import get_current_user
from sqlalchemy.orm import Session
from db.repository.file import create_file
from db.models.user import User

from db.sessions import get_db

router = APIRouter()


@router.post("/file/upload-file", response_model=ShowFile)
async def upload_file(file: UploadFile, data: CreateFile = Depends(), db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        file_path = f"upload/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())
            fileindb = create_file(db=db, file=file, author_id=current_user.id, blog_id=data.blog_id)
            return fileindb
    except Exception as e:
        return {"error": str(e.args)}
