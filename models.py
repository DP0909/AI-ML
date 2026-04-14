from sqlalchemy import Column, Integer, String, DateTime
from database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    company_name = Column(String)
    document_type = Column(String)
    uploaded_by = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)