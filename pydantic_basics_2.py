from pydantic import BaseModel, Field, computed_field, EmailStr, HttpUrl, ValidationError

class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

class FileSchema(BaseModel):
    id: str
    url: HttpUrl
    filename: str
    directory: str

class CourseSchema(BaseModel):
    id: str 
    title: str = 'course-title-default'
    created_by_user: UserSchema
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    preview_file: FileSchema = Field(alias='previewFile')
    description: str
    estimated_time: str = Field(alias='estimatedTime')

#обработка ошибки
try:
    file = FileSchema(
    id = "1",
    url = 'localhost',
    filename = 'plane.png',
    directory = 'courses'
    )
except ValidationError as error:
    print(error)
    print(error.errors)