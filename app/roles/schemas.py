from pydantic import BaseModel

class RoleCreate(BaseModel):
    name: str
    description: str

class RoleUpdate(BaseModel):
    name: str | None = None
    description: str | None = None

class RoleAssignPermissions(BaseModel):
    permission_ids: list[int]
