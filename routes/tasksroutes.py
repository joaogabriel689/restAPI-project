from fastapi import APIRouter
from datetime import datetime
from schema.taskschema import TaskCreate, TaskResponse, TaskStatus, TaskSchema

app_tasks = APIRouter(prefix="/tasks", tags=["Tasks"])



@app_tasks.get("/", response_model=list[TaskSchema])
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
@app_tasks.get("/{task_id}", response_model=TaskSchema)
async def read_task(task_id: int):
    return {
        "id": task_id,
        "title": "Sample Task",
        "description": "This is a sample task description.",
        "status": False,
        "user_id": 1,
        "created_at": "2024-01-01T00:00:00Z"
    }
@app_tasks.post("/", response_model=TaskResponse)
async def create_task(task: TaskCreate):
    return {
        "id": 1,
        "title": task.title,
        "description": task.description,
        "status": TaskStatus.pending,
        "user_id": 1,
        "created_at": datetime.utcnow()
    }

@app_tasks.put("/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, task: TaskCreate):
    updated_task = task.model_dump()
    updated_task["id"] = task_id
    return updated_task
@app_tasks.delete("/{task_id}")
async def delete_task(task_id: int):
    return {"message": f"Task with id {task_id} has been deleted."}