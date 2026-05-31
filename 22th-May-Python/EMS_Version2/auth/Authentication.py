from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from datetime import datetime
from ..dbConfig import engine
from models.Model import Employee, Role
from ..dbConfig import get_db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()
router= FastAPI(title="Employee Authentication System")
db= get_db()

class LoginCredentials(BaseModel):
    email: str
    password: str

class RegisterCredentials(BaseModel):
    fname = Column(String(100))
    lname = Column(String(100))
    phone = Column(String(10))
    gmail = Column(String(100), unique=True)
    dept = Column(String(50))
    role = Role.role_id
    salary = Column(Integer)

@router.post('/login')
def login(login_data:LoginCredentials, db: Session = Depends(get_db)):
    email = login_data.email
    password = login_data.password
    try:
        user = db.query(Employee).filter(
            Employee.gmail == email,
            Employee.password == password
        ).first()
        if user is not None:
            return user
    except Exception as e:
        raise HTTPException(status_code=404, detail="Incorrect email or password")

@router.post('/register')
def register(registerCredentials:RegisterCredentials, db= Session(bind=engine)):
    employee = Employee(registerCredentials.fname,registerCredentials.lname,registerCredentials.phone,registerCredentials.gmail,registerCredentials.dept,registerCredentials.role,registerCredentials.salary)
    db.add(employee)
    db.commit()
    return {
        'message': 'Registration Successful',
    }
