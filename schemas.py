from pydantic import BaseModel
from typing import Optional


# API through aaune data lai validate garna ko lagi schemas ko use garincha

class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    
    class Config:                                   # configuration
        orm_mode = True                             # by default, orm_mode = False huncha, so orm_mode lai True gareko
        schema_extra = {                            # schema_extra chai khas frontend developer ko lagi sajilo vaos vanera ho
            'example':{
                "username": "test",
                "email": "test@gmail.com",
                "password": "password"
            }
        }



class SignUpResponseModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    class Config:
	    orm_mode=True



class LoginModel(BaseModel):
    username:str
    password:str

    class Config:
	    orm_mode=True



class Settings(BaseModel):
    authjwt_secret_key:str='c082810ee1a9d31b433353d0f217375aad9741f795cd5e68bb4576d017da320d'


class OrderModel(BaseModel):
    id: Optional[int]
    plate_quantity: int
    order_status: Optional[str]="PENDING"
    pizza_size: Optional[str]="MEDIUM"
    user_id: Optional[int]


    class Config:
        orm_mode = True
        schema_extra= {
            "example":{
                "plate_quantity":1,
                "pizza_size":"MEDIUM"
            }
        }


class OrderStatusModel(BaseModel):
    order_status: Optional[str]="PENDING"

    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "order_status": "PENDING"
            }
        }
        
        
    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "order_status":"PENDING"
            }
        }
    

