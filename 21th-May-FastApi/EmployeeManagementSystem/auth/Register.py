# auth/Register.py
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from model.Employee import Employee
from dbConfig.DBConnection import get_db

class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str
    department: str
    salary: float

router = APIRouter()  # rename from 'app' to 'router'

@router.post("/register")
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    existing_user = db.query(Employee).filter(Employee.email == data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_employee = Employee(
        empname=data.name,
        email=data.email,
        password=data.password,
        dept=data.department,
        salary=data.salary
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return {
        "message": "User registered successfully",
        "name": new_employee.empname
    }