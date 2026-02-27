from pydantic import BaseModel, ConfigDict, Field
from clients.courses.course_schema import CourseSchema


class ExerciseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    """
    Описание структуры создания упражнения
    """

    id: str
    title: str
    course_id: str = Field(alias="courseId")
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
    exercises: list[ExerciseSchema]

class GetExerciseResponseSchema(BaseModel):
    exercise: ExerciseSchema

class CreateExerciseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

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
    exercise: ExerciseSchema

class UpdateExerciseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    """
    Описание структуры запроса на обновление упражнения.
    """ 
    title: str |None
    max_score: int |None = Field(alias="maxScore")
    min_score: int |None = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str |None
    estimated_time:  str|None = Field(alias="estimatedTime")
class UpdateExerciseResponseSchema(BaseModel):
    exercise: ExerciseSchema