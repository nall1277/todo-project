from datetime import datetime
from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    createdAt: datetime
    done: bool | None = False


class TodoCreate(TodoBase):
    pass


class TodoList(TodoBase):
    id: int

    class Config:
        orm_mode = True
