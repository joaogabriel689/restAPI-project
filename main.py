
from fastapi import FastAPI
from app.users import models as user_models
from app.sales import models as sales_models
from app.inventory import models as inventory_models
from app.reports import models as reports_models
from app.products import models as product_models
from app.database.database import engine
from app.database.database import Base


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Main API")
@app.get("/")
async def root():
    return {"message": "Welcome to the Main API"}




