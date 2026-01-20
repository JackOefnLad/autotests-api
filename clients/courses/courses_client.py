from clients.api_client import APIClient
from httpx import Response, Request
from typing import TypedDict

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
    def update_course_api(self,request, course_id: str) -> Response:
        return self.patch(f"/api/v1/courses/{course_id}")
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