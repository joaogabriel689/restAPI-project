from fastapi import APIRouter, Depends, HTTPException, status

app_users = APIRouter(prefix="/users", tags=["users"])

@app_users.get("/{user_id}")
async def get_user(user_id: int):
    return {"message": f"Get user with ID {user_id}"}
 
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