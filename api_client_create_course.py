from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import CreateUserRequestDict, get_public_users_client, CreateUserRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from tools.fakers import get_random_email
import os

os.environ["NO_PROXY"] = "*"  # отключение прокси

public_users_client = get_public_users_client()
create_user_request = CreateUserRequestDict(
    email = get_random_email(),
    password = "string",
    lastName = "string",
    firstName = "string",
    middleName =  "string",
)
create_user_response = public_users_client.create_user(create_user_request)
print(create_user_response)

authentication_user = AuthenticationUserSchema(
    email = create_user_request['email'],
    password = create_user_request['password']
)

files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)

create_file_request = CreateFileRequestDict(
    filename = 'plane.png',
    directory = 'courses',
    upload_file = './testdata/files/plane.png'
)
create_file_response =  files_client.create_file(create_file_request)
print(create_file_response)

create_course_request = CreateCourseRequestDict(
    title = 'test name',
    maxScore = 100,
    mixScore = 10,
    description = 'lorem ipsum',
    estimatedTime = "2 weeks",
    previewFileId = create_file_response['file']['id'],
    createdByUser = create_user_response['user']['id']
)
create_course_response = courses_client.create_course(create_course_request)
print(create_course_response) 