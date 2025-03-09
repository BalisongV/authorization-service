# словарь для хранения пользователей

fake_users_db = {
    "johndoe": {
        "user_id": 1,
        "name": "John Doe",
        "age": 30,
        "email": "johndoe@example.com",
        "role": "user",
        "hashed_password": "hashed_password_123",  # здесь будет хэширование
    },
    "admin": {
        "user_id": 2,
        "name": "Admin",
        "age": 35,
        "email": "admin@example.com",
        "role": "admin",
        "hashed_password": "hashed_password_456",  # здесь будет хэширование
    },
}