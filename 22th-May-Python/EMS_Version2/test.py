from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Request Body Model
class User(BaseModel):
    name: str
    age: int

# API Method
@app.put("/users/{user_id}")
def update_user(
    user_id: int,          # Path Parameter
    active: bool,          # Query Parameter
    user: User             # Request Body
):
    return {
        "path_param": user_id,
        "query_param": active,
        "body": user
    }

@app.get('/user')
def getUser(user:User):

    return user