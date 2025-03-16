from fastapi import APIRouter, Depends, Response, Header
from models.user import User
from dependencies.auth import authenticate_user, check_allow_edit

router = APIRouter()

@router.post("/signin")
def signin(response: Response, x_username: str = Header(...), x_user_hashed_password: str = Header(...)): #Зачем здесь заголовки? Не надо
    print(user)
    user_credentials:dict = json.loads(response.body)
    curr_user = user_credentials.get('login', None)
    
    # каким-то образом взять из fake_db данные из словаря по ключу curr_user
    
    # далее проводишь авторизацию
    user = authenticate_user(x_username, x_user_hashed_password)
    
    
    # response.headers["X-Username"] = x_username
    # response.headers["X-User-Hashed-Password"] = x_user_hashed_password
    # response.headers["X-Allow-Edit"] = "True"
    
    return user

@router.get("/me")
def read_current_user(user: User = Depends(authenticate_user), allow_edit: bool = Depends(check_allow_edit)):
    return user