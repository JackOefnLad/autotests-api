from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

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