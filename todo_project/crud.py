from sqlalchemy.orm import Session
from . import models, schemas

def get_todolist(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TodoList).offset(skip).limit(limit).all()


