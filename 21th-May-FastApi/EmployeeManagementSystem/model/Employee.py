from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Employee(Base):
    __tablename__ = "Employee"

    empid = Column(Integer, primary_key=True, index=True)
    empname = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String(100))
    dept = Column(String(50))
    salary = Column(Integer)