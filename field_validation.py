from pydantic import BaseModel, Field

class Employee(BaseModel):
    name:str = Field (
        ...,
        min_length=6,
        max_length=12,
        description="Employee Name"
    )
    salary:int = Field(
        ...,
        gt= 25000,
        lt=150000,

    )
    email_id:str = Field(
        default=""
    )
emp = Employee(name= "Jeeshan", salary=140000)
print(emp)