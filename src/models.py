from sqlalchemy import Column, Integer, String, Date
from database import Base

class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)
    dob = Column(Date,nullable=False)
    email = Column(String,index=True,unique=True,nullable=False)
    password = Column(String, nullable=False)