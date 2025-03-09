from fastapi import APIRouter, Depends, Response
from models.user import User
from dependencies.auth import authenticate_user, check_allow_edit

router = APIRouter()

@router.post("/signin")
def signin(response: Response, user: User = Depends(authenticate_user)):
    response.headers["X-Allow-Edit"] = "True"
    return user

@router.get("/me")
def read_current_user(user: User = Depends(authenticate_user), allow_edit: bool = Depends(check_allow_edit)):
    return user