from fastapi import APIRouter, Depends
from models.user import User
from dependencies.auth import authenticate_user

router = APIRouter()

@router.post("/signin")
def signin(user: User = Depends(authenticate_user)):
    return user

@router.get("/me")
def read_current_user(user: User = Depends(authenticate_user)):
    return user