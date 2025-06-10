#вся логика здесь
#создание задачи, получение всех, получение одной по айди, удаление по айди

# def function_name(db: Session, данные):
#     # 1. Создать или получить объект
#     # 2. Добавить в db (если Create)
#     # 3. Commit
#     # 4. Вернуть результат

from sqlalchemy.orm import Session
from . import models
from . import schemas

def create_task(db:Session, task_data:schemas.TaskCreate):
    task = models.Task(**task_data.dict())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_all_tasks(db: Session):
    return db.query(models.Task).all()

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if task:
        db.delete(task)
        db.commit()
        return task
    return None