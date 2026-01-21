from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict
from public_http_builder import get_public_http_client


class CreateUserDict(TypedDict):
    """
    Описание запроса для создания пользователя
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """
    def create_user_api(self, request: CreateUserDict) -> Response:
        """
        Метод создания пользователя
        :request: Словарь с данными для создания пользоваеля
        :return: Ответ от сервера в виде объекта
        """
        return self.post("/api/v1/users", json=request)
    
def get_public_users_client() -> PublicUsersClient: 
    """
    Функция создаёт экземпляр PublicUsersClient с базовыми настройками.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())