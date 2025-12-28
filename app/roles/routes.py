from fastapi import APIRouter, Depends, HTTPException, status
from app.depends.depends import require_admin
from app.roles import models as role_models
from app.database.database import get_db
from app.core.security import verify_access_token
from .schemas import RoleCreate, RoleUpdate, roleAssignPermissions


app_roles = APIRouter(prefix="/roles", tags=["roles"])

@app_roles.get("/")
async def list_roles(admin=Depends(require_admin), db=Depends(get_db)):
    roles = db.query(role_models.Role).all()
    return roles
       

@app_roles.post("/")
async def create_role(role: RoleCreate,
            admin=Depends(require_admin),
            db=Depends(get_db)):
    
    existing = db.query(role_models.Role).filter_by(name=role.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Role already exists")

    

    role_model = role_models.Role(name=role.name, description=role.description)
    db.add(role_model)
    db.commit()
    db.refresh(role_model)
    return {"message": f"Create a new role {role.name}"}

@app_roles.put("/{role_id}")
async def update_role(
    role_id: int,
    role: RoleUpdate,
    admin=Depends(require_admin),
    db=Depends(get_db)
):
    role_model = db.query(role_models.Role).filter_by(id=role_id).first()
    if not role_model:
        raise HTTPException(status_code=404, detail="Role not found")

    if role.name is not None:
        role_model.name = role.name
    if role.description is not None:
        role_model.description = role.description

    db.commit()
    return {"message": f"Role {role_id} updated"}




@app_roles.delete("/{role_id}")
async def delete_role(role_id: int,
            admin=Depends(require_admin),
            db=Depends(get_db)): 
    #dar atençao
    if role.name == "admin":
        raise HTTPException(400, "Admin role cannot be deleted")

    if not db.query(role_models.Role).filter(role_models.Role.id == role_id).first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")
    db.query(role_models.Role).filter(role_models.Role.id == role_id).delete()
    db.commit()

    return {"message": f"Delete role with ID {role_id}"}









#dar atençao as 2 rotas abaixo
@app_roles.get("/{role_id}/permissions")
async def get_role_permissions(role_id: int,admin=Depends(require_admin),db=Depends(get_db)):
    user_roles = db.query(role_models.Role).filter(role_models.Role.id == role_id).first()
    return {"message": f"Get permissions for role with ID {role_id}",
            "roles": user_roles.permissions
            }







@app_roles.post("/{role_id}/permissions")
async def assign_permissions_to_role(
    role_id: int,
    data: roleAssignPermissions,
    admin=Depends(require_admin),
    db=Depends(get_db)
):
    role = db.query(role_models.Role).filter_by(id=role_id).first()
    if not role:
        raise HTTPException(404, "Role not found")

    permissions = db.query(role_models.Permission)\
        .filter(role_models.Permission.id.in_(data.permission_ids))\
        .all()

    role.permissions = permissions
    db.commit()

    return {"message": "Permissions assigned successfully"}