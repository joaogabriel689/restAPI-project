from fastapi import APIRouter, Depends, HTTPException, status

app_cash_register = APIRouter(prefix="/cash-register", tags=["cash-register"])

@app_cash_register.get("/status/")
async def get_cash_register_status():
    return {"status": "operational"}

@app_cash_register.post("/open/")
async def open_cash_register():
    return {"status": "cash register opened"}

@app_cash_register.post("/close/")
async def close_cash_register():
    return {"status": "cash register closed"}   

@app_cash_register.get("/transactions/")
async def get_cash_register_transactions():
    return [{"transaction_id": 1, "amount": 100.0, "type": "sale"}]