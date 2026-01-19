from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class LoginRequest(TypedDict):
    email: str
    password: str

class RefreshToken(TypedDict):
    refreshToken: str

class AuthenticationClient(APIClient):
    def login_api(self, request:LoginRequest) -> Response:
        return self.post("/api/v1/authentication/login", json=request)
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
    def refresh_api(self, request: RefreshToken) -> Response:
        return self.post("/api/v1/authentication/refresh", json=request)
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """