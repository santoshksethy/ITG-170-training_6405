from sqlalchemy.orm import Session
from app.crud import user as crud
from app.schemas.user import UserCreate, UserUpdate

def create_user(db: Session, user: UserCreate):
    return crud.create_user(db, user)

def get_user(db: Session, user_id: int):
    return crud.get_user(db, user_id)

def get_users(db: Session, skip: int, limit: int, search: str):
    return crud.get_users(db, skip, limit, search)

def update_user(db: Session, user_id: int, user: UserUpdate):
    return crud.update_user(db, user_id, user)

def delete_user(db: Session, user_id: int):
    return crud.delete_user(db, user_id)