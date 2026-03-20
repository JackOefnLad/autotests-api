from http import HTTPStatus
from clients.authentication.authentication_schema import LoginResponseSchema, LoginRequestSchema
from clients.users.user_schema import CreateUserRequestSchema
from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from tools.assertions.base import assert_status_code
from tools.assertions.authentication import assert_login_response
from fixtures.users import UserFixture
from jsonschema import validate
import pytest

@pytest.mark.authentication
@pytest.mark.regression
def test_login(function_user:UserFixture, authentication_client:AuthenticationClient):
    
    request = LoginRequestSchema(
        email=function_user.email,
        password=function_user.password
    )
    # print(f"\nRequesting URL: {authentication_client.client.base_url}/api/v1/authentication/login")

    response = authentication_client.login_api(request)
    # print(f"Status Code: {login_response.status_code}")
    # print(f"Response Text: {login_response.text}")
    response_data=LoginResponseSchema.model_validate_json(response.text)
    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_login_response(response_data)

    validate(response.json(), response_data.model_json_schema())

