from fastapi import APIRouter, Depends, HTTPException, status


app_inventory = APIRouter(prefix="/inventory", tags=["inventory"])


@app_inventory.get("/")
async def read_inventory():
    return {"message": "Inventory home"}

@app_inventory.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id < 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return {"item_id": item_id, "name": f"Item {item_id}"}

@app_inventory.post("/entry/")
async def create_item(name: str):
    return {"item_id": 1, "name": name}


@app_inventory.post("/adjustment/")
async def restock_item(item_id: int, quantity: int):
    if quantity <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Quantity must be positive")
    return {"item_id": item_id, "restocked_quantity": quantity}

