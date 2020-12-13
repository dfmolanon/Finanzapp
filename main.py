from db.login_db import UserInDB
from db.login_db import update_user, get_user,create_user

from models.login_models import UserIn, UserOut, NewUserIn
from fastapi import FastAPI
from fastapi import HTTPException
api = FastAPI()

@api.post("/user/login/")
async def login_user(user_in: UserIn):
    user_in_db = get_user(user_in.username)
    if user_in_db == None:
        raise HTTPException(status_code=404,detail="El usuario no existe")
    if user_in_db.password != user_in.password:
        return {"Autenticado": False}
    return {"Autenticado": True}

@api.post("/user/register/")
async def new_user(new_user_in: NewUserIn):
    new_user_db=create_user(new_user_in)
    user_in_db = get_user(new_user_db.username)
    return user_in_db
  
@api.get("/")
async def home():
    return {"message": "Bienvenido a Finanzapp"}

@api.get("/user/{username}")
async def get_username(username: str):
    login_in_db = get_user(username)
    if login_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    user_out = UserOut(**login_in_db.dict())
    return user_out