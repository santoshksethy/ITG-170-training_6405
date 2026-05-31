from datetime import datetime
from typing import Any

from pydantic import BaseModel
from enum import Enum
from datetime import datetime

from sqlalchemy import Column, Integer
from sqlalchemy.orm import mapped_column

from dbConfig.DBConnection import Base


class Department(BaseModel):
    department_id: str
    department_name: str

class Role(BaseModel):
    role_id: str
    role :str

class Status(Enum):
    a = "active"
    i = "inactive"
    p = "assigned"
    b = "bench"

class Employee(Base):
    __tablename__ = "Employee"
    empid = Column(Integer, primary_key=True, index=True)
    fname: str
    lname: str
    phone: str
    pmail: str
    cmail:str
    password:str
    dept: Department.department_id
    role: Role.role_id
    salary: float
    status: Status.a
    join_date: datetime

    def __init__(self, fname, lname, phone, pmail, cmail, dept, role, salary, **kw: Any):
        super().__init__(**kw)
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.pmail = pmail
        self.cmail = self.getCorporateMail(fname,lname)
        self.password = self.createPassword(fname,lname)
        self.dept = dept
        self.role = role
        self.salary = salary
        self.status = Status.a
        self.join_date = datetime.now()

    def getCorporateMail(self,fname,lname):
        return f"{self.fname[0]}{self.lname}@company.com"

    
    def createPassword(self,fname,lname):
        now= datetime.now()
        return f'{self.fname[-2:]}{self.lname[:2]}{now.strftime("%H%M%d")}'
