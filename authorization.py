# импорты библиотек
from fastapi import APIRouter, HTTPException, Response, Request
from pydantic import BaseModel
import jwt
import hashlib

# импорты из файлов
import config as c
# from middleware_auth import redis_client

router = APIRouter()



security = c.AuthX(config=c.config)

class UserLoginSchema(BaseModel):
    username: str
    password: str



# функции
# def get_current_user(request: Request):
#     token = request.cookies.get(c.config.JWT_ACCESS_COOKIE_NAME)  
#     if not token:
#         raise HTTPException(status_code=401, detail="JWT токен отсутствует")
    
#     try:
#         payload = jwt.decode(token, c.config.JWT_SECRET_KEY, algorithms=["HS256"])  
#         return payload  
    
#     except jwt.ExpiredSignatureError:
#         raise HTTPException(status_code=401, detail="Срок действия токена истек")
    
#     except jwt.InvalidTokenError:
#         raise HTTPException(status_code=401, detail="Некорректный токен")

# роуты
# @app.post('/login')
# def login(creds: UserLoginSchema, response: Response, request:Request):
#     # if creds.username == 'user1' and creds.password == 'secret_password':
#     #     access_token = security.create_access_token(uid='123456')
#     #     response.set_cookie(c.config.JWT_ACCESS_COOKIE_NAME, access_token)  
#     #     response.headers["X-Allow-Edit"] = "TRUE"
#     #     return {'access_token': access_token}

#     # raise HTTPException(status_code=401, detail='Неверное имя пользователя или пароль')
#     stored_password_hash = redis_client.get(creds.username)
#     if stored_password_hash is None:
#         raise HTTPException(status_code=403, detail="User not found")

#     password_hash = hashlib.sha256(creds.password.encode()).hexdigest()
#     if password_hash != stored_password_hash:
#         raise HTTPException(status_code=403, detail="Incorrect password")

#     return {"message": "Login successful"}


# data = {key: redis_client.get(key) for key in redis_client.keys("*")}
# print(data)


#, dependencies=[Depends(security.access_token_required)]
# @app.get('/protected')
# def protected(user=Depends(get_current_user)): 
#     return {
#         'message':'Доступ разрешен',
#         'data': 'TOP SECRET',
#         'user': user
#         }

@router.get("/get_users")
async def get_users(request: Request):
    if not request.state.has_creds:
        raise HTTPException(status_code=400, detail='Отсутствует логин или пароль')
    return {"users": ["user1", "user2", "user3"]}

@router.post("/add_new_user")
async def add_new_user(request: Request):
    if not request.state.allow_edit:
        raise HTTPException(status_code=403, detail="Отказано в доступе")
    return {"message": "Пользователь добавлен"}

@router.delete("/delete_user")
async def delete_user(request: Request):
    if not request.state.allow_edit:
        raise HTTPException(status_code=403, detail="Отказано в доступе")
    return {"message": "Пользователь удален"}
