from pydantic import BaseModel

class RoleCreate(BaseModel):
    name: str
    description: str

class RoleUpdate(BaseModel):
    id: int
    name: str | None = None
    description: str | None = None