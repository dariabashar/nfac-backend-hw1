from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud
from . import schemas
from .database import get_db

router = APIRouter()

@router.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@router.get("/tasks/", response_model=list[schemas.Task])
def get_all_tasks(db:Session = Depends(get_db)):
    return crud.get_all_tasks(db)

@router.get("/tasks/{task_id}", response_model=schemas.Task)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.get("/tasks/", response_model=list[schemas.Task])
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_task(db, task_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"ok": True}
