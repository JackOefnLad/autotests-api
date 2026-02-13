from clients.api_client import APIClient
from clients.courses.courses_client import Course
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client

from httpx import Response
from typing import TypedDict

class Exercise(TypedDict):
  id: str
  title: str
  courseId: Course['id']
  maxScore: 0
  minScore: 0
  orderIndex: 0
  description: str
  estimatedTime: str
class GetExercisesQueryDict(TypedDict):
    courseId:   str
    """
    Описание структуры запроса на получение списка упражнений.
    """

class GetExercisesResponseDict(TypedDict):
    exercises: list[Exercise]

class GetExerciseResponseDict(TypedDict):
    exercise: Exercise

class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание упражнения.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str
class CreateExerciseResponseDict(TypedDict):
    exercise: Exercise

class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление упражнения.
    """ 
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime:  str
class UpdateExerciseResponseDict(TypedDict):
    exercise: Exercise

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка упражнений.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)
    
    def get_exercise_api(self, exercise_id: str) -> GetExerciseResponseDict:
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
    
    def get_exercises(self, request: GetExercisesQueryDict)-> GetExercisesResponseDict:
        """
        Метод для получения списка заданий.
        Выполняет запрос и возвращает JSON-ответ.
        """        
        response = self.get_exercises_api(request)
        return response.json()
    def get_exercise(self, exercise_id: str)-> GetExerciseResponseDict:
        """
        Метод для получения конкретного задания по ID.
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()
    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        """
        Метод для создания задания.
        """
        response = self.create_exercise_api(request)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict)-> GetExercisesResponseDict:
        response = self.create_exercise_api(request)
        return response.json()
    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        """
        Метод для обновления задания.
        """
        response = self.update_exercise_api(exercise_id, request)
        return response.json()
    
def get_exercise_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExerciseClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExerciseClient.
    """
    return ExercisesClient(client=get_private_http_client(user))