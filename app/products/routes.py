from fastapi import APIRouter, Depends, HTTPException, status


app_products = APIRouter(prefix="/products", tags=["products"])

@app_products.get("/", summary="Get all products")
async def get_all_products():
    # Logic to retrieve all products
    return {"message": "List of all products"}

@app_products.get("/{product_id}", summary="Get a product by ID")
async def get_product_by_id(product_id: int):
    # Logic to retrieve a product by ID
    if product_id != 1:  # Example condition
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return {"message": f"Details of product {product_id}"}

@app_products.post("/", summary="Create a new product")
async def create_product(product: dict):
    # Logic to create a new product
    return {"message": "Product created", "product": product}

@app_products.put("/{product_id}", summary="Update a product by ID")
async def update_product(product_id: int, product: dict):
    # Logic to update a product by ID
    if product_id != 1:  # Example condition
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return {"message": f"Product {product_id} updated", "product": product}

@app_products.delete("/{product_id}", summary="Delete a product by ID")
async def delete_product(product_id: int):
    # Logic to delete a product by ID
    if product_id != 1:  # Example condition
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return {"message": f"Product {product_id} deleted"}

@app_products.patch("/{product_id}/activate", summary="Activate a product by ID")
async def activate_product(product_id: int):
    # Logic to activate a product by ID
    if product_id != 1:  # Example condition
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return {"message": f"Product {product_id} activated"}
@app_products.patch("/{product_id}/deactivate", summary="Deactivate a product by ID")
async def deactivate_product(product_id: int):
    # Logic to deactivate a product by ID
    if product_id != 1:  # Example condition
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return {"message": f"Product {product_id} deactivated"}