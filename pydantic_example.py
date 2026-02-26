from pydantic import BaseModel, Field

class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    id: str
    name: str
    age: int
    is_active: bool = True
    
    address: Address

ad1 = Address(city="Saint-Petersburgh", zip_code="190000")

user = User(id="1",
            name="John",
            age=20, 
            address=ad1
            #address={'city':"Moscow", 'zip_code':"10000"
            #address: Address(city="Saint-Petersburgh", zip_code="190000"
            )
print(user.address.city)
#Преобразование из модели в словарь
user.model_dump()
#Преобразование из модели в JSON-строка
user.model_dump_json()
 
#Aliases
class CourseSchema(BaseModel):
    id: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
