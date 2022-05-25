from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id : int = Field(default=None)
    function : str = Field(default=None)
    equation : str = Field(default=None)
    class Config:
        schema_extra = {
            "post_demo": {
                "function" : "some function",
                "equation" : "some equation"
            }
        }
        
class UserSchema(BaseModel):
    fullname : str = Field(default=None)
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        the_schema = {
            "user_demo" : {
                "name" : "Plug",
                "email" : "plugpyprch@gmail.com",
                "password" : "1234"
            }
        }
        
class UserLoginSchema(BaseModel):
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        the_schema = {
            "user_demo" : {
                "email" : "plugpyprch@gmail.com",
                "password" : "1234"
            }
        }