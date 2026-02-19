from pydantic import BaseModel, Field, field_validator, model_validator

class Register(BaseModel):
    username: str = Field(..., max_length=10, min_length=4)
    password: str
    re_password: str
    mobile: int 

    @field_validator('mobile')
    def validate_mobile(cls, value):
        if len(str(value)) != 10:
            raise ValueError('mobile number must be 10 digit')
        
        if str(value)[0] not in ['9', '8', '7']:
            raise ValueError('mobli number start with 9,8,7')
        
        return value
    
    @model_validator(mode='after')
    def pass_validator(self):
        if self.password != self.re_password:
            raise ValueError('password not match')
        
        if len(self.password) < 8:
            raise ValueError('password must be 8 digit')
        
        return self

    
new_register = Register(username= "Jeeshan", password='12312312', re_password='12312312', mobile= 9898989898 )

print(new_register)
