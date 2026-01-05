# Дополнительные команды

1. Дополнительные команды по установке и управлению VENV
Создание - python -m venv myenv 
Запуск venv - .\myenv\Scripts\activat
Запуск сервера - uvicorn main:app --reload
Запуск gRPC сервера - python -m grpc_server
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser - позволяет запускать скрипты для профиля (из прописанной директории)



Репозиторий с API от автора - https://github.com/Nikita-Filonov/qa-automation-engineer-api-course

### Порядок для развертывания сервера на новой машине
1) Запустить venv
2) pip install -r requirements.txt для установки зависимостей
3) Создать .env и заполнить его данными:

~APP_HOST="http://localhost:8000"

DATABASE_URL="sqlite+aiosqlite:///./local.db"

JWT_ALGORITHM="HS256"
JWT_SECRET_KEY="qa-automation-engineer-api-course-secret-key"
JWT_ACCESS_TOKEN_EXPIRE=1800
JWT_REFRESH_TOKEN_EXPIRE=5184000~
