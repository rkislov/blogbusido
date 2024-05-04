from sqlalchemy.orm import Session

from schemas.user import UserCreate
from db.models.user import User
from core.hashing import Hasher
from uuid import uuid4


def create_new_user(db: Session, user: UserCreate) -> User:
    user = User(
        email=user.email,
        password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
