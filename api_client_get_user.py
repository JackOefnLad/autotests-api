from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from clients.users.private_users_client import get_private_users_client
from clients.private_http_builder import AuthenticationUserDict
from tools.fakers import get_random_email

import os

os.environ["NO_PROXY"] = "*"  # отключение прокси

public_users_client = get_public_users_client()
create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
create_user_response = public_users_client.create_user_api(create_user_request)
create_user_response_data = create_user_response.json()

authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)
private_users_client = get_private_users_client(authentication_user )

get_user_response = private_users_client.get_user_api(create_user_response_data['user']['id'])
get_user_response_data = get_user_response.json()

print("Get user data: ", get_user_response_data)