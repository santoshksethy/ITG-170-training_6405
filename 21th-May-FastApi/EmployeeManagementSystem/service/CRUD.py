# CRUD.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel, EmailStr

from dbConfig.DBConnection import SessionLocal
from model.Employee import Employee  # SQLAlchemy model
from pydantic import BaseModel, constr

router = APIRouter()  # Router to be included in main.py


# ---------------------------
# Pydantic Schemas
# ---------------------------

class EmployeeCreate(BaseModel):
    empname: str
    email: EmailStr
    password: str
    dept: Optional[str] = None
    salary: Optional[float] = None


class EmployeeUpdate(BaseModel):
    empname: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    dept: Optional[str]
    salary: Optional[float]

    model_config = {"from_attributes": True}  # Pydantic v2


class EmployeeRead(BaseModel):
    empid: int
    empname: str
    email: EmailStr
    dept: Optional[str]
    salary: Optional[float]

    model_config = {"from_attributes": True}  # Pydantic v2

class PasswordUpdate(BaseModel):
    new_password: constr(min_length=6)  # enforce minimum password length

# ---------------------------
# Database Dependency
# ---------------------------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------------------
# CRUD Endpoints
# ---------------------------

# CREATE Employee
@router.post("/", response_model=EmployeeRead)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    new_employee = Employee(**employee.dict())
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee


# READ All Employees
@router.get("/", response_model=List[EmployeeRead])
def read_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()


# READ Employee by ID
@router.get("/{empid}", response_model=EmployeeRead)
def read_employee(empid: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.empid == empid).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


# UPDATE Employee
@router.put("/{empid}", response_model=EmployeeRead)
def update_employee(empid: int, emp_update: EmployeeUpdate, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.empid == empid).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    for key, value in emp_update.dict(exclude_unset=True).items():
        setattr(employee, key, value)

    db.commit()
    db.refresh(employee)
    return employee


# DELETE Employee
@router.delete("/{empid}")
def delete_employee(empid: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.empid == empid).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(employee)
    db.commit()
    return {"detail": "Employee deleted"}


@router.patch("/employees/{empid}/password", tags=["Employees"])
def update_password(empid: int, password_data: PasswordUpdate, db: Session = Depends(get_db)):
    # Fetch employee
    employee = db.query(Employee).filter(Employee.empid == empid).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    # Update password
    employee.password = password_data.new_password
    db.commit()
    db.refresh(employee)

    return {"message": "Password updated successfully"}