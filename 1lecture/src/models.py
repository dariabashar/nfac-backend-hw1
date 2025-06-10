#описание таблиц (какие поля будут в базе)
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from src.database import Base 

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    deadline = Column(DateTime, nullable=True)
    completed = Column(Boolean, default=False)