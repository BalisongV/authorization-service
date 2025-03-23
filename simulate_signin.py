import httpx

def simulate_signin():
    # URL эндпоинта /signin
    url = "http://127.0.0.1:8001/signin"
    
    # Данные для отправки
    data1 = {
        "username": "johndoe",
        "password": "password123"
    }

    data2 = {
        "username": "johndoe",
        "password": "pasafjfieha"
    }
    
    data_list = [data1, data2]

    for i in range(0, len(data_list)):

        # POST-запрос
        with httpx.Client() as client:
            response = client.post(url, json=data_list[i])
        
        # Результат
        if response.status_code == 200:
            print("Success!")
            print("Response:", response.json())
        else:
            print("Error:", response.status_code)
            print("Message:", response.json())


# Запуск асинхронной функции
if __name__ == "__main__":
    simulate_signin()