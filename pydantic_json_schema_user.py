from clients.users.public_users_client import get_public_users_client
from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake
import jsonschema  # type: ignore
import os

os.environ["NO_PROXY"] = "*"  # отключение прокси


public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
# Используем метод create_user
create_user_response = public_users_client.create_user_api(create_user_request)
create_user_response_schema = CreateUserResponseSchema.model_json_schema()
print(create_user_response)
print(create_user_response_schema)
# jsonschema.validate(instance=create_user_response.json(), schema=create_user_response_schema)

validate_json_schema(instance=create_user_response.json(), schema=create_user_response_schema)