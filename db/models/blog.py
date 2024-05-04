from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from fastapi_utils.guid_type import GUID
from db.base import Base


class Blog(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    slug = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    author = relationship('User', back_populates='blogs')
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    is_active = Column(Boolean, nullable=False, default=True)
