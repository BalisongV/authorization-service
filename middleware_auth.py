import hashlib
import redis
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
import logging

logging.basicConfig(
    format='%(asctime)s - %(message)s', 
    datefmt='%d-%b %H:%M:%S', 
    level=logging.INFO, 
    filename="app.log", 
    filemode="a", 
    encoding='utf8',
    force=True
    )

redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

password = "secret_password"
hashed_password = hashlib.sha256(password.encode()).hexdigest()
redis_client.set("user_password_hash", hashed_password)




class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        x_allow_edit = request.headers.get("X-Allow-Edit")
        request.state.allow_edit = False
        request.state.has_creds = False

        if x_allow_edit and x_allow_edit.upper() == "TRUE":
            username = request.headers.get("X-Username")
            password = request.headers.get("X-User-Hashed-Password")

            if not username or not password:
                logging.error('Username or password is missing')
                raise HTTPException(status_code=400, detail="Username or password is missing")
            else:
                request.state.has_creds = True
            
            stored_password_hash = redis_client.get(username)

            if stored_password_hash is None:
                logging.error('User not found')
                raise HTTPException(status_code=403, detail="User not found")
            
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            
            if isinstance(stored_password_hash, bytes):
                stored_password_hash = stored_password_hash.decode()

            if password_hash != stored_password_hash:
                logging.error('Incorrect password')
                raise HTTPException(status_code=403, detail="Incorrect password")

            request.state.allow_edit = True

        
        logging.info(f"Headers: {dict(request.headers)}\n--------------------------------")
        # logging.info(f"Stored hash: {stored_password_hash}, Computed hash: {password_hash}")
        response = await call_next(request)
        return response