import asyncio
import websockets

async def websocket_client():
    uri = "ws://localhost:8765"
    
    try:
        async with websockets.connect(uri) as websocket:
            print("Успешно подключено к серверу")
            
            # Отправляем сообщение серверу
            message = "Привет, сервер!"
            await websocket.send(message)
            print(f"Отправлено серверу: {message}")
            
            # Получаем 5 ответных сообщений от сервера
            print("Ожидание ответов от сервера...")
            for i in range(5):
                response = await websocket.recv()
                print(f"Получено от сервера: {response}")
            
            print("Все 5 сообщений получены!")
            
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Ошибка: Соединение закрыто сервером: {e}")
    except ConnectionRefusedError:
        print("Ошибка: Не удалось подключиться к серверу. Убедитесь, что сервер запущен на ws://localhost:8765")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

if __name__ == "__main__":
    asyncio.run(websocket_client())