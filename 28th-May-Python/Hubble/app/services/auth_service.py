from ..models.employee import Employee
from ..db.session import SessionLocal
from ..core.security import verify_password

def authenticate_user(gmail: str, password: str):
    db = SessionLocal()
    user = db.query(Employee).filter(Employee.gmail == gmail).first()
    db.close()

    if not user:
        return None

    if not verify_password(password, user.password):
        return None

    return user