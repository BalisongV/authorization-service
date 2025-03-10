# импорт библиотек
import uvicorn
import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# импорты из файлов
from authorization import router as test_router
from routers.auth import router as auth_router
from middleware_auth import AuthMiddleware

# http://127.0.0.1:8000/docs#/


'''
Для запуска прописать в терминал:

fastapi dev main.py

или

uvicorn main:app --host localhost --port 8001 --reload

или

python main.py

'''
app1 = FastAPI()
app2 = FastAPI()

origins = [
       "http://localhost:8001/",
       "http://localhost:8000/",
       "http://127.0.0.1:8000/",
       "http://127.0.0.1:8001/",
       ]
app1.include_router(test_router)
app2.include_router(auth_router)

app2.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"], 
                   allow_headers=["*"],  
                   )
app1.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"], 
                   allow_headers=["*"],  
                   )
app1.add_middleware(AuthMiddleware)


async def run_server(app, port):
    config = uvicorn.Config(app, host="127.0.0.1", port=port, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    await asyncio.gather(
        run_server(app1, 8000),
        run_server(app2, 8001),
    )
# запуск

if __name__ == '__main__':
#     uvicorn.run('main:app', reload=True, host='localhost', port=8001)
       asyncio.run(main())