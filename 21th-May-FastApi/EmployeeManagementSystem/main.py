from fastapi import FastAPI
from dbConfig.DBConnection import Base, engine  # <-- Base comes from DB connection / models
from auth.Register import router as register_router
from service.CRUD import router as employee_router  # <-- only import router here
from auth.Login import router as login_router
from auth.Logout import router as logout_router  # your logout file


# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Management System")

# Include routers
routers= [login_router, register_router, logout_router]

for router in routers:
    app.include_router(router, prefix="/auth", tags=["auth"])
app.include_router(employee_router, prefix="/employees", tags=["Employees"])