from pydantic import BaseModel, ConfigDict, Field
from clients.files.files_schema import FileSchema
from clients.users.user_schema import UserSchema

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
    title: str
    max_score: int |None = Field(alias='maxScore')
    min_score: int |None = Field(alias='minScore')
    description: str
    preview_file_id: str = Field(alias='previewFileId')
    estimated_time: str |None = Field(alias='estimatedTime')
    created_by_user_id: str = Field(alias='createdByUser')


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
    title: str | None
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    description: str | None
    estimated_time: str | None = Field(alias='estimatedTime')
