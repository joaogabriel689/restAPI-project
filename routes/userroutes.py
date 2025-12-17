from fastapi import APIRouter
from datetime import datetime
from app.auth import hash_password, verify_password
from schema.userschema import UserResponse, UserCreate, UserSchema
from schema.authschema import LoginRequest, TokenResponse
from app.database import engine

app_user = APIRouter(prefix="/users", tags=["Users"])

@app_user.get("/me", response_model=UserSchema)
async def read_user_me():
    return {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "password": "securepassword",
        "created_at": "2024-01-01T00:00:00Z"
    }

@app_user.get("/{user_id}", response_model=UserSchema)
async def read_user(user_id: int):
    return {
        "id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "password": "securepassword",
        "created_at": "2024-01-01T00:00:00Z "
    }


@app_user.post("/auth/register", response_model=UserResponse)
async def create_user(user: UserCreate):
    email = user.email
    password_hashed = hash_password(user.password)




@app_user.post("/auth/login", response_model=TokenResponse)
async def login_user(data: LoginRequest):
    return {
        "access_token": "fake-jwt-token"
    }






