from fastapi import APIRouter, Depends, HTTPException, status
from app.users.schemas import UserCreate
from app.users.models import User
from app.auth.auth import verify_user, get_user_by_email
from app.auth.schemas import LoginRequest, TokenJwt, TokenRequest
from app.auth.models import BlackListToken
from app.database.database import get_db
from app.auth.auth import hash_password, verify_password
from app.core.security import create_access_token
from datetime import timedelta


app_auth = APIRouter(prefix="/auth", tags=["auth"])


#fazer login
@app_auth.post("/login")
async def login(login_data: LoginRequest, db=Depends(get_db)):  
    email = login_data.email
    password_request = login_data.password
    user = get_user_by_email(email, db=db)  
    if (user is None) or (verify_password(password_request, user.password) == False) or (user.is_active == False):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password."
        )
    else:
        dict_user = {
            "sub": str(user.id),
            "name": user.name,
            "email": user.email,
            "iat": timedelta.utcnow().timestamp(),
            "role": [user.role]
            
        }
        deltatime = timedelta(minutes=60)
        access_token = create_access_token(data=dict_user, expires_delta=deltatime)
        return {"access_token": access_token, "token_type": "bearer"}




#registrar ususario
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



#fazer logout
@app_auth.post("/logout")
async def logout(token: TokenRequest, db=Depends(get_db)):
    blacklisted_token = BlackListToken(token=token.token)
    db.add(blacklisted_token)
    db.commit()
    return {"message": "Logout endpoint"}