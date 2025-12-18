'''from fastapi import APIRouter, Depends, HTTPException, status
from app.sales.models import Sale
from app.sales.schemas import SaleCreate, SaleResponse

app_sales = APIRouter(prefix="/sales", tags=["sales"])
@app_sales.post("/", response_model=SaleResponse)
async def create_sale(sale: SaleCreate):
    # Logic to create a sale
    new_sale = Sale(id=1, **sale.dict())
    return new_sale

@app_sales.post("/{id}/items/", response_model=SaleResponse)
async def add_item_to_sale(sale_id: int, item_id: int, quantity: int):
    # Logic to add an item to a sale
    return Sale(id=sale_id, item_id=item_id, quantity=quantity, total_price=100.0)

@app_sales.put("/{sale_id}/items/{item_id}", response_model=SaleResponse)
async def update_item_in_sale(sale_id: int, item_id: int, quantity: int):
    # Logic to update an item in a sale
    return Sale(id=sale_id, item_id=item_id, quantity=quantity, total_price=100.0)

@app_sales.delete("/{sale_id}/items/{item_id}", response_model=SaleResponse)
async def remove_item_from_sale(sale_id: int, item_id: int):
    # Logic to remove an item from a sale
    return Sale(id=sale_id, item_id=item_id, quantity=0, total_price=0.0)

@app_sales.put("/{sale_id}/finalize", response_model=SaleResponse)
async def finalize_sale(sale_id: int):
    # Logic to finalize a sale
    return Sale(id=sale_id, item_id=1, quantity=2, total_price=100.0)

@app_sales.get("/{sale_id}", response_model=SaleResponse)
async def read_sale(sale_id: int):
    # Logic to read a sale by ID
    if sale_id < 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sale not found")
    return Sale(id=sale_id, item_id=1, quantity=2, total_price=100.0)

@app_sales.get("/")
async def read_sales():
    # Logic to read all sales
    return [{"id": 1, "item_id": 1, "quantity": 2, "total_price": 100.0}]

@app_sales.delete("/{sale_id}", response_model=dict)
async def delete_sale(sale_id: int):
    # Logic to delete a sale
    return {"detail": f"Sale {sale_id} deleted"}

@app_sales.get("/users/{user_id}/sales", response_model=list[SaleResponse])
async def read_sales_by_user(user_id: int):
    # Logic to read sales by user ID
    return [Sale(id=1, item_id=1, quantity=2, total_price=100.0)]

@app_sales.get("/sale-items/{sale_item_id}", response_model=SaleResponse)
async def read_sale_item(sale_item_id: int):
    # Logic to read a sale item by ID
    return Sale(id=1, item_id=sale_item_id, quantity=2, total_price=100.0)
Docstring for app.sales.routes
'''

