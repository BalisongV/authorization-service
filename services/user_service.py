from database.fake_db import fake_users_db
from models.user import User

# логика для работы с пользователями

def get_user(username: str, hashed_password: str) -> User | None:
    user_data = fake_users_db.get(username)
    if user_data and user_data["hashed_password"] == hashed_password:
        return User(**user_data)
    return None