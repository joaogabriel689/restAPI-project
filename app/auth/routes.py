from fastapi import APIRouter, Depends, HTTPException, status
from app.users.schemas import UserCreate
from app.users.models import User
from .auth import verify_user
from app.database.database import get_db
from app.auth.auth import hash_password, verify_password

app_auth = APIRouter(prefix="/auth", tags=["auth"])

@app_auth.post("/login")
async def login():
    return {"message": "Login endpoint"}

@app_auth.post("/register")
async def register(user: UserCreate, db=Depends(get_db)):
    email = user.email
    user_role = user.role
    password = hash_password(user.password)
    name = user.name
    if verify_user(email, db=db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists."
        )
    else:
        dict_user = User(
            name=name,
            email=email,
            password=password,
            role=user_role
        )
        db.add(dict_user)
        db.commit()
        db.refresh(dict_user)
        return {"message": "user registered successfully"}

@app_auth.post("/refresh-token")
async def refresh_token():
    return {"message": "Refresh token endpoint"}

@app_auth.post("/logout")
async def logout():
    return {"message": "Logout endpoint"}