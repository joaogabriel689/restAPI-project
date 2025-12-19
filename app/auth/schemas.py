from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str



class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    sub: str | None = None
    name: str | None = None
    email: EmailStr | None = None
    iat: float | None = None
    roles: list[str] = []
class TokenRequest(BaseModel):
    token: str  
