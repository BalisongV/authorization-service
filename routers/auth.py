from fastapi import APIRouter, Depends, Response, Header
from models.user import User
from dependencies.auth import authenticate_user
import json
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/signin")
def signin(login_data: LoginRequest):
    header_data = authenticate_user(login_data.username, login_data.password)
    
    return header_data

@router.get("/me")
def read_current_user(user: User = Depends(authenticate_user)):
    return user

