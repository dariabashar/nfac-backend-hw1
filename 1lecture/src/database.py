#соединение с базой

from typing import List
from sqlalchemy import create_engine #подключение к постгресу через sql alchemy, 
#^ импорт функции, чтобы создать движок подключения к бд
from sqlalchemy.ext.declarative import declarative_base #импорт функции для создания базового класса моделей
#все таблицы будут наследоваться отсюда
from sqlalchemy.orm import sessionmaker #позволяет нам создать сессию (объект, с помощью которого мы делаем sql запросы)

DATABASE_URL = "postgresql://postgres:password@localhost:5432/mydb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()