from pydantic import BaseModel

class LoginSchema(BaseModel):
    gmail: str
    password: str