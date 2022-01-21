from sqlalchemy import Boolean, Column, Integer, String, DateTime
from .database import Base


class TodoList(Base):
    __tablename__ = "todo_list"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    createdAt = Column(DateTime)
    done = Column(Boolean, default=False)
