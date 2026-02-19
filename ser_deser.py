from pydantic import BaseModel, model_validator

class Students(BaseModel):

    name:str
    age:int
    email:str
    branch:str
    address:str
    sem:int

data = {
    "name":"rahul",
    "age":28,
    "email":"rahul@123gmail.com",
    "branch":"CSE",
    "address":'Mumbai',
    "sem":5,
}

# Student = Students(**data)      # ser
# print(Student)

Student = Students.model_validate(data)   # deser
print(Student)