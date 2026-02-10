from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_http_client
from clients.users.user_schema import CreateUserRequestSchema
from tools.fakers import get_random_email

public_users_client = get_public_http_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password='string',
    last_name='string',
    first_name='string',
    middle_name='string',
)

create_user_response=public_users_client.create_user()