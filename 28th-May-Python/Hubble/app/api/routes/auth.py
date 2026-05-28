from fastapi import APIRouter, HTTPException
from ....app.schemas.auth import LoginSchema
from ....app.services.auth_service import authenticate_user
from ....app.core.jwt import create_access_token

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