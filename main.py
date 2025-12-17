from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import datetime
class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str
    created_at: datetime

class Task(BaseModel):
    id: int
    title: str
    description: Union[str, None] = None
    status: bool
    user_id: int
    created_at: datetime

app = FastAPI()

@app.post("/auth/register", response_model=User)
async def create_user(user: User):
    return user
@app.post("/auth/login")
async def login_user(email: str, password: str):
    return {"message": "Login successful", "email": email}


@app.get("/users/me", response_model=User)
async def read_user_me():
    return {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "password": "securepassword",
        "created_at": "2024-01-01T00:00:00Z"
    }

@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    return {
        "id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "password": "securepassword",
        "created_at": "2024-01-01T00:00:00Z "
    }











@app.get("/tasks/", response_model=list[Task])
async def read_tasks():
    return [
        {
            "id": 1,
            "title": "Sample Task 1",
            "description": "This is the first sample task.",
            "status": False,
            "user_id": 1,
            "created_at": "2024-01-01T00:00:00Z"
        },
        {
            "id": 2,
            "title": "Sample Task 2",
            "description": "This is the second sample task.",
            "status": True,
            "user_id": 1,
            "created_at": "2024-01-02T00:00:00Z"
        }
    ]
@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int):
    return {
        "id": task_id,
        "title": "Sample Task",
        "description": "This is a sample task description.",
        "status": False,
        "user_id": 1,
        "created_at": "2024-01-01T00:00:00Z"
    }
@app.post("/tasks/", response_model=Task)
async def create_task(task: Task):
    return task 
@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: Task):
    updated_task = task.model_dump()
    updated_task["id"] = task_id
    return updated_task
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    return {"message": f"Task with id {task_id} has been deleted."}