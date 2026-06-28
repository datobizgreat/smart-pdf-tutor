"""
Database models
Phase 11 - PostgreSQL Integration
"""

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()


class User(Base):
    """User model for authentication"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    documents = relationship("Document", back_populates="user")
    chats = relationship("Chat", back_populates="user")


class Document(Base):
    """Document model for uploaded PDFs"""
    __tablename__ = "documents"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    filename = Column(String(255), nullable=False)
    file_path = Column(String(500), nullable=False)
    total_pages = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="documents")
    chats = relationship("Chat", back_populates="document")


class Chat(Base):
    """Chat history model"""
    __tablename__ = "chats"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="chats")
    document = relationship("Document", back_populates="chats")
