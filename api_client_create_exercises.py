from clients.users.public_users_client import get_public_users_client
from clients.files.files_client import get_files_client
from clients.private_http_builder import AuthenticationUserSchema
from clients.courses.courses_client import get_courses_client
from clients.exercises.exercises_client import get_exercise_client
from clients.users.user_schema import CreateUserRequestSchema
from clients.files.files_schema import CreateFileRequestSchema
from clients.courses.course_schema import CreateCourseRequestSchema
from clients.exercises.exercise_schema import CreateExerciseRequestSchema


from tools.fakers import get_random_email
import os

os.environ["NO_PROXY"] = "*"  # отключение прокси

# Создаем пользователя
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
public_users_client = get_public_users_client()

create_user_response = public_users_client.create_user(create_user_request)

# Инициализируем клиенты
authentication_user = AuthenticationUserSchema( 
    email=create_user_request.email,
    password=create_user_request.password
)
files_client = get_files_client(authentication_user)

create_file_request = CreateFileRequestSchema(
    filename="plane.png",
    directory="courses",
    upload_file="./testdata/files/plane.png"
)
create_file_response = files_client.create_file(create_file_request)

# 3. Инициализируем клиент курсов (с авторизацией)
courses_client = get_courses_client(authentication_user)

# Создаем курс
print("Создание курса...")
create_course_request = CreateCourseRequestSchema(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id
)
create_course_response = courses_client.create_course(create_course_request)
course_id = create_course_response.course.id
print(f"Курс создан, ID: {course_id}")

# 4. Инициализируем клиент заданий (с авторизацией)
exercises_client = get_exercise_client(authentication_user)

# Создаем задание
print("Создание задания...")
exercise_request = CreateExerciseRequestSchema(
    title="Первое тестовое задание",
    courseId=course_id,
    maxScore=10,
    minScore=0,
    orderIndex=1,
    description="Выполните задание",
    estimatedTime="30 minutes"
)

create_exercise_response = exercises_client.create_exercise(exercise_request)
print(f"Задание создано: {create_exercise_response}")
