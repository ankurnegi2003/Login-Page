from pydantic import BaseModel, EmailStr
from datetime import date

class Signin(BaseModel):
    email:EmailStr
    password: str 

class Signup(BaseModel):
    name:str
    dob:date  
    email:EmailStr
    password: str 

class Profileout(BaseModel):
    id:int
    name: str
    dob: date
    email:EmailStr
    class Config:
        orm_mode=True

class DeleteProfile(BaseModel):
    email:EmailStr
    password: str 