from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.messages import get_message
from app.dependencies.db import get_db
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.core.response import APIResponse
from app.services import user_service as service

router = APIRouter(prefix="/users", tags=["Users"])


# CREATE (Request Body)
@router.post("/", response_model=APIResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = service.create_user(db, user)

    return APIResponse(
        message=get_message("USER_CREATED"),
        data=UserResponse.model_validate(db_user)
    )


# READ ALL (Query Params)
@router.get("/", response_model=APIResponse)
def get_users(
    skip: int = 0,
    limit: int = 10,
    search: str = Query(None, description="Search by name"),
    db: Session = Depends(get_db)
):
    users = service.get_users(db, skip, limit, search)

    return APIResponse(
        message=get_message("USERS_FETCHED"),
        data=[UserResponse.model_validate(u) for u in users]
    )


# READ ONE (Path Param)
@router.get("/{user_id}", response_model=APIResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = service.get_user(db, user_id)

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    return APIResponse(
        message=get_message("USER_FETCHED"),
        data=UserResponse.model_validate(db_user)
    )


# UPDATE (Path + Body)
@router.put("/{user_id}", response_model=APIResponse)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    updated_user = service.update_user(db, user_id, user)

    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")

    return APIResponse(
        message=get_message("USER_UPDATED"),
        data=UserResponse.model_validate(updated_user)
    )


# DELETE (Path Param)
@router.delete("/{user_id}", response_model=APIResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted_user = service.delete_user(db, user_id)

    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")

    return APIResponse(
        message=get_message("USER_DELETED"),
        data=None
    )