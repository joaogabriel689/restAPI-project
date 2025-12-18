from fastapi import APIRouter, Depends, HTTPException, status


app_auth = APIRouter(prefix="/auth", tags=["auth"])

@app_auth.post("/login")
async def login():
    return {"message": "Login endpoint"}

@app_auth.post("/register")
async def register():
    return {"message": "Register endpoint"}

@app_auth.post("/refresh-token")
async def refresh_token():
    return {"message": "Refresh token endpoint"}

@app_auth.post("/logout")
async def logout():
    return {"message": "Logout endpoint"}