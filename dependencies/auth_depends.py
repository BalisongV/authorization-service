from fastapi import HTTPException, Header
from services.user_service import get_user
from models.user import User

def authenticate_user(x_username: str = Header(...), x_user_hashed_password: str = Header(...)) -> User:
    user = get_user(x_username, x_user_hashed_password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Custom"},
        )
    # return RedirectResponse(url='http://localhost:8000/', status_code=302)
    return user

def check_allow_edit(x_allow_edit: str = Header(...)):
    if x_allow_edit != "True":
        raise HTTPException(status_code=403, detail="Editing not allowed")