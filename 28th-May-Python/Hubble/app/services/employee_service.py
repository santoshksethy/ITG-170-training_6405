from ..db.session import SessionLocal
from ..models.employee import Employee
from ..core.security import hash_password

def create_employee(data):
    db = SessionLocal()

    emp = Employee(
        fname=data.fname,
        lname=data.lname,
        gmail=data.gmail,
        password=hash_password(data.password),
        dept=data.dept,
        sal=data.sal,
        role_id=data.role_id,
        status_id=data.status_id
    )

    db.add(emp)
    db.commit()
    db.refresh(emp)
    db.close()
    return emp


def update_employee(emp_id, data):
    db = SessionLocal()
    emp = db.query(Employee).filter(Employee.emp_id == emp_id).first()

    if not emp:
        db.close()
        return None

    for key, value in data.dict(exclude_unset=True).items():
        setattr(emp, key, value)

    db.commit()
    db.refresh(emp)
    db.close()
    return emp