from fastapi import APIRouter, Depends, HTTPException, status



app_roles = APIRouter(prefix="/roles", tags=["roles"])

@app_roles.get("/")
async def list_roles():
    return {"message": "List all roles"}            

@app_roles.post("/")
async def create_role():
    return {"message": "Create a new role"}

@app_roles.put("/{role_id}")
async def update_role(role_id: int):
    return {"message": f"Update role with ID {role_id}"}

@app_roles.delete("/{role_id}")
async def delete_role(role_id: int):    
    return {"message": f"Delete role with ID {role_id}"}

@app_roles.get("/{role_id}/permissions")
async def get_role_permissions(role_id: int):
    return {"message": f"Get permissions for role with ID {role_id}"}

@app_roles.post("/{role_id}/permissions")
async def assign_permissions_to_role(role_id: int):
    return {"message": f"Assign permissions to role with ID {role_id}"}