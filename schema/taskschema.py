from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class TaskStatus(str, Enum):
    pending = "pending"
    done = "done"

class TaskCreate(BaseModel):
    title: str
    description: str | None = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: TaskStatus
    user_id: int
    created_at: datetime
class TaskSchema(BaseModel):
    id: int
    title: str
    description: str | None
    status: bool
    user_id: int
    created_at: datetime