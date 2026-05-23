from fastapi import APIRouter

router = APIRouter()

@router.post("/logout")
def logout():
    # Since login is stateless, "logging out" just means
    # the client should delete their stored info (e.g., localStorage)
    return {"message": "Logged out successfully"}