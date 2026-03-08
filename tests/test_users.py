from clients.users.public_users_client import get_public_users_client
from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema
from http import HTTPStatus
from jsonschema import validate
from tools.assertions.base import assert_status_code
from tools.assertions.user import assert_create_user_response
import pytest

@pytest.mark.users
@pytest.mark.regression
def test_create_user():
    public_user_client = get_public_users_client()

    request = CreateUserRequestSchema()
    response_create_user = public_user_client.create_user_api(request)
    response_create_user_data = CreateUserResponseSchema.model_validate_json(response_create_user.text)
    
    # assert response_create_user.status_code == HTTPStatus.OK
    assert_status_code(response_create_user.status_code, HTTPStatus.OK)
    assert_create_user_response(request, response_create_user_data)

    validate(response_create_user.json(), response_create_user_data.model_json_schema())