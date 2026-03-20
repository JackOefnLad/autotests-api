from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from http import HTTPStatus
from jsonschema import validate
from tools.assertions.base import assert_status_code
from tools.assertions.user import assert_create_user_response
from clients.users.private_users_client import PrivateUsersClient
from fixtures.users import UserFixture
from tools.assertions.users import assert_get_user_response
import pytest

@pytest.mark.users
@pytest.mark.regression
def test_create_user(public_user_client:PublicUsersClient):

    request = CreateUserRequestSchema()
    response_create_user = public_user_client.create_user_api(request)
    response_create_user_data = CreateUserResponseSchema.model_validate_json(response_create_user.text)
    
    # assert response_create_user.status_code == HTTPStatus.OK
    assert_status_code(response_create_user.status_code, HTTPStatus.OK)
    assert_create_user_response(request, response_create_user_data)

    validate(response_create_user.json(), response_create_user_data.model_json_schema())

@pytest.mark.users
@pytest.mark.regression
def test_get_user_me(private_users_client: PrivateUsersClient, function_user: UserFixture):
    """
    Тест проверяет получение информации о текущем пользователе.
    Эндпоинт: GET /api/v1/users/me
    """    
    response = private_users_client.get_user_me_api()
    assert response.status_code == HTTPStatus.OK
    response_data = GetUserResponseSchema.model_validate(response.json())
    assert_get_user_response(response_data, function_user.response)