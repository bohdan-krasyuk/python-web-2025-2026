import json

from pydantic import BaseModel


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def map_to_json(self):
        return {
            "name": self.__name,
            "age": self.age
        }




# serializing (python data type -> json)
person1 = Person(name="John", age=30)


json_string = json.dumps(person1.map_to_json())

print(json_string)


# deserializing (json -> python data type)


person_json_string = '{"name": "John", "age": 30}'
person_json_dict = json.loads(person_json_string)

if len(person_json_dict['name']) < 2:
    print("Name must be at least 2 characters long")

person_from_json = Person(
    name=person_json_dict["name"],
    age=person_json_dict["age"]
)

print(person_from_json.age)



# deserializing with pydantic
class PersonDto(BaseModel):
    name: str
    age: int

raw_dictionary = {
    "name": "John",
    "age": 30
}

person_dto = PersonDto(**raw_dictionary)
print(person_dto)

raw_json_string = '{"name": "John", "age": 30}'
person_dto_from_string = PersonDto.model_validate_json(raw_json_string)
print(person_dto_from_string)


# serializing with pydantic
person_dto_to_json = person_dto.model_dump_json()
print(person_dto_to_json)
print(type(person_dto_to_json))

print(person_dto_from_string.model_dump())
print(type(person_dto_from_string.model_dump()))
