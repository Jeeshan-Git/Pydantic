from pydantic import BaseModel, Field
from typing import Annotated

class user(BaseModel):
    name:Annotated[str, Field(..., min_length = 8)]
    age:Annotated[int, Field(..., ge=18)]

user = user(name='Jeeshan good work', age= 28)
print(user)

    