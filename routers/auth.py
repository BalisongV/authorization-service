from fastapi import APIRouter, Depends, Response, Header
from fastapi.responses import RedirectResponse
import webbrowser

from models.user import User
from dependencies.auth_depends import authenticate_user, check_allow_edit

router = APIRouter()

@router.post("/signin")
def signin(response: Response, x_username: str = Header(...), x_user_hashed_password: str = Header(...)):
    user = authenticate_user(x_username, x_user_hashed_password)

    response.headers["X-Username"] = x_username
    response.headers["X-User-Hashed-Password"] = x_user_hashed_password
    response.headers["X-Allow-Edit"] = "True"
    webbrowser.open_new_tab('http://localhost:8000/docs#/')
    return RedirectResponse(url='http://localhost:8000/docs#/', status_code=302)

@router.get("/me")
def read_current_user(user: User = Depends(authenticate_user), allow_edit: bool = Depends(check_allow_edit)):
    return user