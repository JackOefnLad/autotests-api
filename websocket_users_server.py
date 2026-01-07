import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        # Логируем полученное сообщение
        print(f"Получено сообщение от пользователя: {message}")
        
        # Отправляем 5 ответных сообщений с порядковыми номерами
        for i in range(1, 6):
            response = f"{i} Сообщение пользователя: {message}"
            await websocket.send(response)
            await asyncio.sleep(0.1)  # Небольшая задержка между сообщениями

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        print("WebSocket сервер запущен на ws://localhost:8765")
        await asyncio.Future()  # Бесконечное ожидание

if __name__ == "__main__":
    asyncio.run(main())