"""
{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "estimatedTime": "string",
  }
}
"""
import uuid
from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel
class CourseSchema(BaseModel):
    # model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = 'course-title-default'
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    description: str
    estimated_time: str = Field(alias='estimatedTime')

course_default_model = CourseSchema(id='1',
                                    title='Api',
                                    maxScore=100,
                                    minScore=10,
                                    description='Course',
                                    estimatedTime='2 weeks'
                                    )
course_dict_model ={                "id":'1',
                                    "title":'Api-dict',
                                    "maxScore":100,
                                    "minScore":10,
                                    "description":'Course-dcit',
                                    "estimatedTime":'2 weeks'
}

course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week"
}
"""

print(course_default_model)
#---------------------------

# print(CourseSchema(**course_dict_model))
#--------------------------
# course_json_model = CourseSchema.model_validate_json(course_json)
# print(course_json_model)
#print(CourseSchema.model_validate_json(course_json))
# print(course_json_model.model_dump()) # сериализация в словарь
# print(course_json_model.model_dump_json(by_alias=True)) # сериализация в json со значениями из alias в модели