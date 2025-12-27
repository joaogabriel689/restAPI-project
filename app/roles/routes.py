from fastapi import APIRouter, Depends, HTTPException, status
from app import depends
from app.depends.depends import require_permission, require_admin, verify_role
from app.roles import models as role_models
from app.database.database import get_db
from app.core.security import verify_access_token
from .schemas import RoleCreate, RoleUpdate


app_roles = APIRouter(prefix="/roles", tags=["roles"])

@app_roles.get("/")
async def list_roles(token=Depends(verify_access_token),db=Depends(get_db)):
    roles = db.query(role_models.Role).all()

    return {"roles": roles}            

@app_roles.post("/")
async def create_role(role: RoleCreate,
            admin=Depends(require_admin),
            db=Depends(get_db)):
    

    role_model = role_models.Role(name=role.name, description=role.description)
    db.add(role_model)
    db.commit()
    db.refresh(role_model)
    return {"message": f"Create a new role {role.name}"}

@app_roles.put("/{role_id}")
async def update_role(role: RoleUpdate,
        admin=Depends(require_admin),
        db=Depends(get_db)):
    
    if not db.query(role_models.Role).filter(role_models.Role.id == role.id).first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")

    role_model = db.query(role_models.Role).filter(role_models.Role.id == role.id).first()
    if role.name is not None:
        role_model.name = role.name
    if role.description is not None:
        role_model.description = role.description

    db.commit()
    db.refresh(role_model)
    return {"message": f"Update role with ID {role.id}"}



@app_roles.delete("/{role_id}")
async def delete_role(role_id: int,token=Depends(verify_access_token),db=Depends(get_db)):    
    return {"message": f"Delete role with ID {role_id}"}

@app_roles.get("/{role_id}/permissions")
async def get_role_permissions(role_id: int,token=Depends(verify_access_token),db=Depends(get_db)):
    return {"message": f"Get permissions for role with ID {role_id}"}

@app_roles.post("/{role_id}/permissions")
async def assign_permissions_to_role(role_id: int,token=Depends(verify_access_token),db=Depends(get_db)):
    return {"message": f"Assign permissions to role with ID {role_id}"}