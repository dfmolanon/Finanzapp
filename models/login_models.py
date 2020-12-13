from pydantic import BaseModel
class UserIn(BaseModel):     #ingresa usuario
    username: str
    password: str
class UserOut(BaseModel):    #return
    username: str
    name:str
    email:str
class NewUserIn(BaseModel):
    username: str
    name: str
    email: str
    password: str


