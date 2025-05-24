# app/api/v1/auth_routes.py

from .jwt_auth import create_access_token
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter()

# Dummy in-memory "user store" for now
FAKE_USERS_DB = {
    "admin": {
        "username": "admin",
        "password": "password123",  # In production, NEVER store plain passwords!
    }
}

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/auth/login")
async def login(request: LoginRequest):
    user = FAKE_USERS_DB.get(request.username)
    if not user or user["password"] != request.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    # Credentials valid -> create JWT
    access_token = create_access_token(data={"sub": request.username})
    return {"access_token": access_token, "token_type": "bearer"}
