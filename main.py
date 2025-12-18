
from fastapi import FastAPI
from app.database import Base, engine
from app.companies import models as company_models
from app.users import models as user_models
from app.inventory import models as inventory_models
from app.products import models as product_models
from app.reports import models as report_models
from app.tributation import models as tributation_models
from app.sales import models as sales_models

from app.cash_register.routes import app_cash_register
from app.inventory.routes import app_inventory
from app.reports.routes import app_reports
from app.sales.routes import app_sales
from app.users.routes import app_users
from app.companies.routes import app_companies
from app.products.routes import app_products
from app.tributation.routes import app_tributation




Base.metadata.create_all(bind=engine)

app = FastAPI(title="Main API")
@app.get("/")
async def root():
    return {"message": "Welcome to the Main API"}




