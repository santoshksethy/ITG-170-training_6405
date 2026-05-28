from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..db.base import Base

class Employee(Base):
    __tablename__ = "employees"

    emp_id = Column(Integer, primary_key=True, index=True)

    fname = Column(String(50))
    lname = Column(String(50))
    phone = Column(String(15))

    gmail = Column(String(100), unique=True, index=True)
    cmail = Column(String(100))

    password = Column(String(255))

    dept = Column(String(50))
    sal = Column(Float)

    joindate = Column(Date)

    role_id = Column(Integer, ForeignKey("roles.role_id"))
    status_id = Column(Integer, ForeignKey("statuses.status_id"))

    role = relationship("Role")
    status = relationship("Status")