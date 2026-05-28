from fastapi import FastAPI
from api.routes import auth, employee
from core.exceptions import global_exception_handler

app = FastAPI(title="Hubble HR System")

app.include_router(auth.router, prefix="/auth")
app.include_router(employee.router, prefix="/api")

app.add_exception_handler(Exception, global_exception_handler)