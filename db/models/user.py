from db.base import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship, Mapped


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    is_superuser = Column(Boolean, nullable=False, default=False)
    is_active = Column(Boolean, nullable=False, default=True)
    blogs = relationship("Blog", back_populates="author")
    files = relationship("File", back_populates="author")

    def __str__(self):
        return self.email
