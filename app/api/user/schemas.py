from pydantic import BaseModel

class UserSchema(BaseModel):
    display_name: str
    email: str
    password: str
    role: str

class ShowUserSchema(BaseModel):
    display_name: str
    email: str

    class config:
        orm_mode = True