import socket
import threading
from queue import Queue

class ChatServer:
    def __init__(self, host='localhost', port=12345, max_connections=10):
        self.host = host
        self.port = port
        self.max_connections = max_connections
        self.message_history = []  # Список всех сообщений
        self.active_connections = 0
        self.lock = threading.Lock()  # Блокировка для безопасного доступа к общим данным
        self.running = True
        
    def handle_client(self, client_socket, client_address):
        """Обработка подключения клиента"""
        print(f"Пользователь с адресом: {client_address} подключился к серверу")
        
        try:
            while True:
                # Получаем данные от клиента
                data = client_socket.recv(1024)
                if not data:
                    break
                
                message = data.decode('utf-8').strip()
                print(f"Пользователь с адресом: {client_address} отправил сообщение: {message}")
                
                # Добавляем сообщение в историю
                with self.lock:
                    self.message_history.append(message)
                
                # Отправляем историю сообщений клиенту
                history_text = '\n'.join(self.message_history)
                client_socket.send(history_text.encode('utf-8'))
                
        except ConnectionError:
            print(f"Соединение с {client_address} разорвано")
        finally:
            # Уменьшаем счетчик активных подключений
            with self.lock:
                self.active_connections -= 1
            client_socket.close()
            print(f"Пользователь с адресом: {client_address} отключился")
    
    def start(self):
        """Запуск сервера"""
        # Создаем TCP сокет
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Устанавливаем опцию для повторного использования адреса
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            # Привязываем сокет к адресу и порту
            server_socket.bind((self.host, self.port))
            
            # Устанавливаем очередь подключений
            server_socket.listen(self.max_connections)
            
            print(f"Сервер запущен на {self.host}:{self.port}")
            print(f"Максимальное количество подключений: {self.max_connections}")
            
            # Основной цикл сервера
            while self.running:
                # Принимаем новое подключение
                client_socket, client_address = server_socket.accept()
                
                # Проверяем количество активных подключений
                with self.lock:
                    if self.active_connections >= self.max_connections:
                        print(f"Достигнут лимит подключений. Отклоняем {client_address}")
                        client_socket.send("Сервер переполнен. Попробуйте позже.".encode('utf-8'))
                        client_socket.close()
                        continue
                    
                    self.active_connections += 1
                
                # Создаем поток для обработки клиента
                client_thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket, client_address),
                    daemon=True
                )
                client_thread.start()
                
        except KeyboardInterrupt:
            print("\nСервер останавливается...")
        except Exception as e:
            print(f"Ошибка сервера: {e}")
        finally:
            server_socket.close()
            print("Сервер остановлен")

def main():
    # Создаем и запускаем сервер
    server = ChatServer()
    server.start()

if __name__ == "__main__":
    main()