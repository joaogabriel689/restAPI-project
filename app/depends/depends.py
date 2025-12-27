from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.security import verify_access_token


security = HTTPBearer()

def get_current_payload(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials
    payload = verify_access_token(token)

    if isinstance(payload, HTTPException):
        raise payload

    return payload


def require_role(role_verified: str):
    def dependency(user = Depends(get_current_payload)):
        if not user.role != role_verified:
            raise HTTPException(status_code=403)
        return user
    return dependency
