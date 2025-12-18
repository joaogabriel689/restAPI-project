from fastapi import APIRouter, Depends, HTTPException, status

app_reports = APIRouter(prefix="/reports", tags=["reports"])

@app_reports.get("/sales-summary/")
async def get_sales_summary():
    return {"total_sales": 1000.0, "number_of_sales": 50}

@app_reports.get("/product-summary/")
async def get_product_summary():
    return {"total_products": 100, "active_products": 80, "inactive_products": 20}

@app_reports.get("/inventory-summary/")
async def get_inventory_summary():
    return {"total_items": 500, "in_stock": 450, "out_of_stock": 50}

@app_reports.get("/export/csv/")
async def export_csv():
    return {"message": "CSV export completed"}

@app_reports.get("/audit-log/")
async def get_audit_log():
    return {"message": "Audit log retrieved"}

@app_reports.get("/audit-log/{entry_id}")
async def get_audit_log_entry(entry_id: int):
    return {"entry_id": entry_id, "message": "Audit log entry retrieved"}