from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from services.db_service import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    date = Column(DateTime, default=datetime.now, nullable=False)
