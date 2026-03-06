from pydantic import BaseModel, ConfigDict, Field
from clients.files.files_schema import FileSchema
from clients.users.user_schema import UserSchema
from tools.fakers import fake


class CourseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    """
    Описание структуры курса.
    """

    id: str
    title: str
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    description: str
    preview_file: FileSchema = Field(alias='previewFile') # Вложенная структура файла 
    estimated_time: str = Field(alias='estimatedTime')
    created_by_user: UserSchema  = Field(alias='createdByUser') # Вложенная структура пользователя


class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    userId: str


class CreateCourseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    """
    Описание структуры запроса на создание курса.
    """
    title: str = Field(default_factory=fake.sentence)
    max_score: int |None = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int |None = Field(alias='minScore', default_factory=fake.min_score)
    description: str = Field(default_factory=fake.sentence)
    preview_file_id: str = Field(alias='previewFileId', default_factory= fake.uuid4)
    estimated_time: str |None = Field(alias='estimatedTime', default_factory = fake.estimated_time)
    created_by_user_id: str = Field(alias='createdByUserId', default_factory= fake.uuid4)


# Добавили описание структуры ответа на создание курса
class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    """
    Описание структуры запроса на обновление курса.
    """
    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int | None = Field(alias='minScore', default_factory=fake.min_score)
    description: str | None = Field(default_factory=fake.sentence)
    estimated_time: str |None = Field(alias='estimatedTime', default_factory = fake.estimated_time)