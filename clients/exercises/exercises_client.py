from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class GetExerciseQueryDict(TypedDict):
    courseId:   str
    """
    Описание структуры запроса на получение списка упражнений.
    """
class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание упражнения.
    """
    title:          str
    courseId:       str
    maxScore:       int
    minScore:       int
    orderIndex:     int
    description:    str
    estimatedTime:  str

class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление упражнения.
    """ 
    title:          str
    maxScore:       int
    minScore:       int
    orderIndex:     int
    description:    str
    estimatedTime:  str

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self, query: GetExerciseQueryDict) -> Response:
        """
        Метод получения списка упражнений.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)
    
    def get_exercises_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения.

        :param exercise_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")
    
    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания упражнения.

        :param request: Словарь с title, courseID, maxScore, minScore, orderIndex, Description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)
    
    def update_exercise_api(self, request:UpdateExerciseRequestDict, exercise_id: str ) -> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)
    
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param course_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")
    