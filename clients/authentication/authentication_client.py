from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict
from public_http_builder import get_public_http_client

class LoginRequest(TypedDict):
    email:      str
    password:   str

class RefreshToken(TypedDict):
    refreshToken:   str
    
class Token(TypedDict):
    tokenType:      str
    accessToken:    str
    refreshToken:   str

class LoginResponse(TypedDict):
    token: Token #Token как объект содержит в себе все параметры из словаря выше 
   
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
    def login(self, request: LoginRequest) -> LoginResponse: 
        """
        Результат выполнения запроса будет записан в response и приведен к json формату
        запрос login_api и запись ответа в .json
        Функция упрощающая получение ответа при запросе и возможность обращаться за токенами
        и прочими данными 
        """
        response = self.login_api(request)
        return response.json()

    # Разобраться лучше в работе этих строк
    """
    Функция get-authentication_client готовит для использования AuthenticationClient
    с помощью функции get_public_http_client, который в свою очередь, готовит экземпляр httpx.Client
    В api_client в клиент передается настроенный клиент
    """
def get_authentication_client() -> AuthenticationClient: 
    return AuthenticationClient(client=get_public_http_client())