from fastapi import APIRouter, HTTPException

from ....app.core.jwt import create_access_token
from ....app.schemas.employee import EmployeeCreate, EmployeeUpdate
from ....app.services.employee_service import create_employee, update_employee
from ..dependencies import get_current_user, require_role

from ....app.schemas.auth import LoginSchema

from services.auth_service import authenticate_user

router = APIRouter()

@router.post("/login")
def login(data: LoginSchema):
    user = authenticate_user(data.gmail, data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({
        "emp_id": user.emp_id,
        "role": user.role.role
    })

    return {"access_token": token}