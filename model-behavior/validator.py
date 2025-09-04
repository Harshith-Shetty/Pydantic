from pydantic import BaseModel, field_validator, model_validator, computed_field


class User(BaseModel):
    userName: str
    password: str


    @field_validator('userName')
    def validate_userName(cls, v):
        if(len(v) < 4):
            raise ValueError("username Error, need more than 4 characters")
        return v
    

class SignUp(BaseModel):
    userNme: str
    password: str
    confirmPassword: str


    @model_validator(mode='after')
    def validate_password(clas, values):
        if(values.password != confirmPassword):
            raise ValueError("password missmatch")
        return values
    
class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_value(self)-> float:
        return self.price * self.quantity
        