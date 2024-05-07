from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from db.base import Base


class File(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    author = relationship('User', back_populates='files')
    blog_id = Column(Integer, ForeignKey('blog.id'), nullable=False)
    blog = relationship('Blog', back_populates='files')
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
