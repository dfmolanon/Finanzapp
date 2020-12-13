from typing import Dict
from pydantic import BaseModel
#definicion db
class UserInDB(BaseModel):
    username: str
    name: str
    email: str
    password: str

#implementacion db
database_users = Dict[str, UserInDB]
database_users = {
    "camilo24": UserInDB(**{"username":"camilo24",
                        "name":"camilo",
                        "email":"camilo2416@gmail.com",
                        "password":"root123"}),
    "andres18": UserInDB(**{"username":"andres18",
                        "name":"andres",
                        "email":"andres-sd@gmail.com",
                        "password":"hola456"}),
}
def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None
def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db
def create_user(new_user: UserInDB):
    database_users[new_user.username]=new_user
    return new_user