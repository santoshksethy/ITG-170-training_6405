from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    fname: str
    lname: str
    gmail: str
    password: str
    dept: str
    sal: float
    role_id: int
    status_id: int

class EmployeeUpdate(BaseModel):
    fname: str | None = None
    lname: str | None = None
    phone: str | None = None