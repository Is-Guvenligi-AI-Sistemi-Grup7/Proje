from fastapi import Depends
from flask import app
from Business.Concrete.UserManager import UserManager

def get_user_service():
    return UserManager()

@app.get("/users/me")
def get_user_info(service: UserManager = Depends(get_user_service)):
    return service.get_current_user()
