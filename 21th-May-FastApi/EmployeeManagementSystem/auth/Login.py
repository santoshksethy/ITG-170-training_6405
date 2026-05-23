from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from dbConfig.DBConnection import get_db
from model.Employee import Employee  # import the SQLAlchemy model



class LoginRequest(BaseModel):
    email: str
    password: str

router = APIRouter()  # 👈 router instance

@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    # Query using SQLAlchemy ORM
    user = db.query(Employee).filter(
        Employee.email == data.email,
        Employee.password == data.password
    ).first()

    if user:
        return {
            "message": f"Welcome {user.empname}!",
            "empid": user.empid,
            "dept": user.dept,
            "salary": user.salary
        }
    else:
        raise HTTPException(status_code=401, detail="Invalid email or password")