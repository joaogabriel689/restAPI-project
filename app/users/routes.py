import token
from fastapi import APIRouter, Depends, HTTPException, status
from app.database.database import get_db
from app.auth.auth import verify_user, get_user_by_email
from app.auth.schemas import LoginRequest, TokenResponse, TokenRequest
from app.core.security import verify_access_token
from app.depends.depends import get_current_payload
from app.users.models import User
from app.users.schemas import UserResponse, UserCreate


app_users = APIRouter(prefix="/users", tags=["users"])


@app_users.get("/me", response_model=UserResponse)
async def get_current_user(
    payload=Depends(get_current_payload),
    db=Depends(get_db)
):
    user = get_user_by_email(payload.get("email"), db=db)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found."
        )

    return user


@app_users.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, payload=Depends(get_current_payload), db=Depends(get_db)):
    user = get_user_by_email(payload.get("email"), db=db)
    if user is None or str(user.id) != str(user_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found."
        )
    return user
 
@app_users.get("/", response_model=list[UserResponse])
async def list_users(payload=Depends(get_current_payload), db=Depends(get_db)):
    if payload.get("role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Operation not permitted."
        )
    users = db.query(User).all()
    return users





@app_users.put("/{user_id}")
async def update_user(user_id: int, user: UserCreate, payload=Depends(get_current_payload), db=Depends(get_db)):
    if payload.get("sub") != str(user_id) :
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Operation not permitted."
        )
    db.query(User).filter(User.id == user_id).update({
        User.name: user.name,
        User.email: user.email,
        User.role: user.role
    })
    db.commit() 
    return {"message": f"Update user with ID {user_id}"}

@app_users.delete("/{user_id}")
async def delete_user(user_id: int, payload=Depends(get_current_payload), db=Depends(get_db)):
    if payload.get("role") == "admin" or str(payload.get("sub")) == str(user_id):
        db.query(User).filter(User.id == user_id).delete()
        db.commit()
        return {"message": f"Delete user with ID {user_id}"}
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Operation not permitted."
    )

@app_users.post("/{user_id}/activate")
async def activate_user(user_id: int, payload=Depends(get_current_payload), db=Depends(get_db)):
    if payload.get("role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Operation not permitted."
        )
    db.query(User).filter(User.id == user_id).update({User.is_active: True})
    db.commit()
    return {"message": f"Activate user with ID {user_id}"}

@app_users.post("/{user_id}/deactivate")
async def deactivate_user(user_id: int, payload=Depends(get_current_payload), db=Depends(get_db)):
    if str(payload.get("sub")) == str(user_id) or payload.get("role") == "admin":
        db.query(User).filter(User.id == user_id).update({User.is_active: False})
        db.commit()
        return {"message": f"Deactivate user with ID {user_id}"}        
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Operation not permitted."
    )