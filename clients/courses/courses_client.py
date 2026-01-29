from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict
from clients.files.files_client import File
from clients.users.private_users_client import User
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema


class GetCoursesQueryDict(TypedDict):
    userId: str
class CreateCourseRequestDict(TypedDict):
    title:              str
    maxScore:           int 
    minScore:           int
    description:        str
    estimatedTime:      str
    previewFileId:      str
    createdByUserId:    str
class UpdateCourseRequestDict(TypedDict):
    title:              str   | None
    maxScore:           int   | None
    minScore:           int   | None
    description:        str   | None
    estimatedTime:      str   | None
class Courses(TypedDict):
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: File  # Вложенная структура файла
    estimatedTime: str
    createdByUser: User  # Вложенная структура пользователя    

class CreateCourseResponseDict(TypedDict):
    course: Courses

class CoursesClient(APIClient):
    def  get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        return self.get("/api/v1/courses", params=query)
    """
    Получение списка курсов
    """
    def get_courses_api(self, course_id: str ) -> Response:
        return self.get(f"/api/v1/courses/{course_id}")
    """
    Получение конкретного курса
    """
    def create_course_api(self, request:CreateCourseRequestDict) -> Response:
        return self.post("/api/v1/courses", json=request)
    """
    Создание курса
    :request: Содержит все необходимые поля для создания курса
    """
    def update_course_api(self,request: UpdateCourseRequestDict, course_id: str) -> Response:
        return self.patch(f"/api/v1/courses/{course_id}", json=request)
    """
    Изменение информации о курсе
    :request: Содержит все необходимые поля для изменения курса
    :course_id: query-параметр для обращения к конкретному курсу
    """
    def delete_course_api(self, course_id : str) -> Response:
        return self.delete(f"/api/v1/courses/{course_id}")
    """
    Изменение информации о курсе
    :course_id: query-параметр для обращения к конкретному курсу
    """

    def create_course(self, request: CreateCourseRequestDict) -> CreateCourseResponseDict:
        response = self.create_course_api(request)
        return response.json()


def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))