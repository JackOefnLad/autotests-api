from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from httpx import Response
from typing import Type, TypedDict

class Token(TypedDict):
    tokenType: str
    accessToken: str
    refreshToken: str

class LoginRequestDict(TypedDict):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str

class refreshRequestDict(TypedDict):
    refreshToken: str

class LoginResponseDict(TypedDict):
    token : Token

class AuthenticationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """
    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/login", json = request)
    
    def refresh_api(self, request: refreshRequestDict) -> Response:
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/refresh", json=request)
    
    def login(self, request: LoginRequestDict)-> LoginResponseDict:
        response = self.login_api(request)
        return response.json()
    
def get_authentication_client () -> AuthenticationClient:
    """
    Функция def_authentication_client готовит(возвращает) AuthenticationClient с параметрами/значениями из get_public_http_client(билдера)
    """
    return AuthenticationClient(client=get_public_http_client)