from pydantic import BaseModel, EmailStr
from typing import Optional

# Base schema
class UserBase(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None


# CREATE request body
class UserCreate(UserBase):
    pass


# UPDATE request body
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None


# RESPONSE model


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None

    class Config:
        from_attributes = True   # ✅ REQUIRED for SQLAlchemy ORM