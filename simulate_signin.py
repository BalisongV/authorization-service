import httpx
import asyncio


async def simulate_signin():
    # URL эндпоинта /signin
    url = "http://127.0.0.1:8001/signin"
    
    # Данные для отправки (username и password)
    data = {
        "username": "johndoe",
        "password": "password123"
    }
    
    # Отправляем POST-запрос
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data)
    
    # Выводим результат
    if response.status_code == 200:
        print("Success!")
        print("Response:", response.json())
    else:
        print("Error:", response.status_code)
        print("Message:", response.json())

# Запуск асинхронной функции
if __name__ == "__main__":
    asyncio.run(simulate_signin())