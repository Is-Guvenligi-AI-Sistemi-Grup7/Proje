from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Any

app = FastAPI()

# DTO modelleri
class UserForLoginDto(BaseModel):
    email: str
    password: str

class UserForRegisterDto(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str

# Servis arayüzü yerine basit stublar
class AuthService:
    def login(self, user_dto: UserForLoginDto) -> dict:
        # Burada gerçek login kontrolü yapılacak
        if user_dto.email != "test@example.com" or user_dto.password != "secret":
            return {"success": False, "message": "Invalid credentials"}
        user_data = {"id": 1, "email": user_dto.email}
        return {"success": True, "data": user_data}

    def create_access_token(self, user_data: dict) -> dict:
        # Burada JWT veya token oluşturma işlemi yapılacak
        token = "fake-jwt-token"
        return {"success": True, "data": {"token": token}}

    def user_exists(self, email: str) -> dict:
        # Kullanıcı var mı kontrolü
        if email == "existing@example.com":
            return {"success": False, "message": "User already exists"}
        return {"success": True}

    def register(self, user_dto: UserForRegisterDto, password: str) -> dict:
        # Kayıt işlemi (örnek)
        user_data = {"id": 2, "email": user_dto.email}
        return {"success": True, "data": user_data}

auth_service = AuthService()

@app.post("/api/auth/login")
def login(user_for_login_dto: UserForLoginDto):
    user_to_login = auth_service.login(user_for_login_dto)
    if not user_to_login["success"]:
        raise HTTPException(status_code=400, detail=user_to_login["message"])

    result = auth_service.create_access_token(user_to_login["data"])
    if result["success"]:
        return result["data"]
    raise HTTPException(status_code=400, detail="Could not create access token")

@app.post("/api/auth/register")
def register(user_for_register_dto: UserForRegisterDto):
    user_exists = auth_service.user_exists(user_for_register_dto.email)
    if not user_exists["success"]:
        raise HTTPException(status_code=400, detail=user_exists["message"])

    register_result = auth_service.register(user_for_register_dto, user_for_register_dto.password)
    result = auth_service.create_access_token(register_result["data"])
    if result["success"]:
        return result["data"]
    raise HTTPException(status_code=400, detail="Could not create access token")
