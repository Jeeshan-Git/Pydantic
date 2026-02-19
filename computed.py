from pydantic import BaseModel, computed_field

class Cartitems(BaseModel):
    user_id:int
    product_id:int
    quantity:int
    price:int

    @computed_field
    @property
    def total_price(self) -> int:
        return self.price * self.quantity
    
cart = Cartitems(user_id= 1, product_id=10, quantity=5, price=100)
print(cart)

