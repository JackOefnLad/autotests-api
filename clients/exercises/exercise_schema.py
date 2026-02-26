from pydantic import BaseModel, ConfigDict, Field
from clients.courses.course_schema import CourseSchema


class Exercise(BaseModel):
  id: str
  title: str
  course_id: CourseSchema['id'] = Field(alias="courseId")
  max_score: int |None = Field(alias="maxScore")
  min_score: int |None = Field(alias="minScore")
  order_index: int = Field(alias="orderIndex")
  description: str
  estimated_time: str |None = Field(alias="estimatedTime")
class GetExercisesQuerySchema(BaseModel):
    courseId:   str
    """
    Описание структуры запроса на получение списка упражнений.
    """

class GetExercisesResponseSchema(BaseModel):
    exercises: list[Exercise]

class GetExerciseResponseSchema(BaseModel):
    exercise: Exercise

class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание упражнения.
    """
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int |None = Field(alias="maxScore")
    min_score: int |None = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str |None = Field(alias="estimatedTime")
class CreateExerciseResponseSchema(BaseModel):
    exercise: Exercise

class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнения.
    """ 
    title: str |None
    max_score: int |None = Field(alias="maxScore")
    min_score: int |None = Field(alias="minScrore")
    order_index: int = Field(alias="orderIndex")
    description: str |None
    estimated_time:  str|None = Field(alias="estimatedTime")
class UpdateExerciseResponseSchema(BaseModel):
    exercise: Exercise