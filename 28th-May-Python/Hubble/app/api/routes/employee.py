from fastapi import APIRouter, Depends
from ....app.schemas.employee import EmployeeCreate, EmployeeUpdate
from ....app.services.employee_service import create_employee, update_employee
from ....app.api.dependencies import require_role, get_current_user

router = APIRouter()

# HR ONLY CREATE EMPLOYEE
@router.post("/employee")
def add_employee(
    data: EmployeeCreate,
    user=Depends(require_role(["h"]))
):
    return create_employee(data)


# EMPLOYEE SELF UPDATE
@router.put("/employee/me")
def update_me(
    data: EmployeeUpdate,
    user=Depends(get_current_user)
):
    return update_employee(user["emp_id"], data)