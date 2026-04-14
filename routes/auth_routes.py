from fastapi import APIRouter
from schemas import UserSchema
from auth import create_token

router = APIRouter()

@router.post("/auth/register")
def register(user: UserSchema):
    return {"msg": "User registered successfully"}

@router.post("/auth/login")
def login(user: UserSchema):
    token = create_token({"sub": user.email})
    return {"access_token": token}