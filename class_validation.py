# from pydantic import BaseModel

# class user(BaseModel):
#     user_id:int
#     age:int
#     name:str
#     is_active:bool

# user = user(user_id = 1, age = 28, name = 'Jeeshan', is_active = True)
# print(user)


from pydantic import BaseModel, PositiveInt
from typing import List, Literal, Optional

class Orders(BaseModel):
    user_id: PositiveInt
    product_id:List[int]
    payment_mode:Literal['online', 'cash']
    delevery_note:Optional[str] = None

order = Orders(user_id = 20, product_id = [10,40,50], payment_mode = 'online', delevery_note = None)
print(order)




