from fastapi import FastAPI
from routers import auth

app = FastAPI()

# Подключаем маршруты
app.include_router(auth.router)

# Запуск приложения
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)