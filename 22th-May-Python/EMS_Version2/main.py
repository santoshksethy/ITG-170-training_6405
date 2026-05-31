from fastapi import FastAPI


app = FastAPI('Employe management system version 2')

routers=[]

for router in routers:
    app.include_router(router, prefix="/auth", tags=["auth"])

