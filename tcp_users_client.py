import socket

def main():
    # Создаем TCP сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Подключаемся к серверу
        client_socket.connect(('localhost', 12345))
        print("Успешно подключился к серверу")
        
        # Отправляем сообщение серверу
        message = "Привет, сервер!"
        client_socket.send(message.encode('utf-8'))
        print(f"Отправил серверу сообщение: {message}")
        
        # Получаем ответ от сервера
        response = client_socket.recv(1024).decode('utf-8')
        print("Ответ от сервера:")
        print(response)
        
    except ConnectionRefusedError:
        print("Ошибка: не удалось подключиться к серверу")
        print("Убедитесь, что сервер запущен на localhost:12345")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        # Закрываем соединение
        client_socket.close()
        print("Соединение закрыто")

if __name__ == "__main__":
    main()