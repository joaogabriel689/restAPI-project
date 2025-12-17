from fastapi import APIRouter, Depends
from datetime import datetime
from app.auth import hash_password, verify_password
from app.security import create_access_token
from schema.userschema import UserResponse, UserCreate, UserSchema
from schema.authschema import LoginRequest, TokenResponse
from app.database import engine, get_db
from models.usermodels import User
from fastapi import HTTPException
from sqlalchemy.orm import Session

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
async def create_user(user: UserCreate, db: Session = Depends(get_db)):



    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user




@app_user.post("/auth/login", response_model=TokenResponse)
async def login_user(data: LoginRequest, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == data.email).first()
    if not existing_user:
        raise HTTPException(status_code=400, detail="Email não cadastrado")
    if not verify_password(data.password, existing_user.password):
        raise HTTPException(status_code=400, detail="Senha incorreta")
    access_token = create_access_token(
        data={"sub": str(existing_user.id),
              "name": existing_user.name,
              "email": existing_user.email,
              "iat": datetime.utcnow().timestamp(),
              "roles": ["user"]
              }
    )

    return {"access_token": access_token, "token_type": "bearer", "user_id": existing_user.id}





