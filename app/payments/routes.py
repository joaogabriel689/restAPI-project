from fastapi import APIRouter, Depends, HTTPException, status


app_payments = APIRouter(prefix="/payments", tags=["payments"])

@app_payments.post("/process/")
async def process_payment(amount: float, payment_method: str):
    if amount <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Amount must be positive")
    return {"status": "success", "amount": amount, "payment_method": payment_method}
@app_payments.get("/status/{payment_id}")
async def get_payment_status(payment_id: int):
    if payment_id < 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
    return {"payment_id": payment_id, "status": "completed"}
