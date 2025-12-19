import token
from fastapi import APIRouter, Depends, HTTPException, status
from app.database.database import get_db
from app.auth.auth import verify_user, get_user_by_email
from app.auth.schemas import LoginRequest, TokenResponse, TokenRequest
from app.core.security import verify_access_token
from app.depends.depends import get_current_payload


app_users = APIRouter(prefix="/users", tags=["users"])

@app_users.get("/{user_id}")
async def get_user(user_id: int, payload=Depends(get_current_payload), db=Depends(get_db)):
    user = get_user_by_email(payload.get("email"), db=db)
    if user is None or str(user.id) != str(user_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found."
        )
    return {"user_id": user.id, "name": user.name, "email": user.email, "role": user.role}
 
@app_users.get("/")
async def list_users():
    return {"message": "List all users"}

@app_users.get("/me")
async def get_current_user():
    return {"message": "Get current authenticated user"}


@app_users.post("/")
async def create_user():
    return {"message": "Create a new user"}


@app_users.put("/{user_id}")
async def update_user(user_id: int):
    return {"message": f"Update user with ID {user_id}"}

@app_users.delete("/{user_id}")
async def delete_user(user_id: int):
    return {"message": f"Delete user with ID {user_id}"}

@app_users.post("/{user_id}/activate")
async def activate_user(user_id: int):
    return {"message": f"Activate user with ID {user_id}"}

@app_users.post("/{user_id}/deactivate")
async def deactivate_user(user_id: int):
    return {"message": f"Deactivate user with ID {user_id}"}