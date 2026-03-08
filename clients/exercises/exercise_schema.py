from pydantic import BaseModel, ConfigDict, Field
from clients.courses.course_schema import CourseSchema
from tools.fakers import fake


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
    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias="courseId", default_factory=fake.uuid4)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex", default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str |None = Field(alias="estimatedTime", default_factory=fake.estimated_time)
class CreateExerciseResponseSchema(BaseModel):
    exercise: ExerciseSchema

class UpdateExerciseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    """
    Описание структуры запроса на обновление упражнения.
    """ 
    title: str |None = Field(default_factory=fake.sentence)
    max_score: int |None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int |None = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex", default_factory=fake.integer)
    description: str |None = Field(default_factory=fake.text)
    estimated_time:  str|None = Field(alias="estimatedTime", default_factory=fake.estimated_time)
class UpdateExerciseResponseSchema(BaseModel):
    exercise: ExerciseSchema
