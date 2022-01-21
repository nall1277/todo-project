from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from . import crud, models, schemas
from .database import SessionLocal, engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_model=list[schemas.TodoList])
async def root(db: Session = Depends(get_db)):
    todo = crud.get_todolist(db)
    return todo
