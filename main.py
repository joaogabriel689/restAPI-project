
from fastapi import FastAPI

from app.database import engine
from app.database import Base
from routes.userroutes import app_user
from routes.tasksroutes import app_tasks


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Main API")
app.include_router(app_user)
app.include_router(app_tasks)
@app.get("/")
async def root():
    return {"message": "Welcome to the Main API"}




