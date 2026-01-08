from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
import models, schemas, logic 

Base.metadata.create_all(bind=engine)
app = FastAPI()
def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

#login to your account
@app.post('/login',response_model=schemas.Profileout)
def logintoyouraccount(details:schemas.Signin, db:Session=Depends(get_db)):
    return logic.signin(db,details)

#signup for new users
@app.post('/signup',response_model=schemas.Profileout)
def createnewaccount(details:schemas.Signup, db:Session=Depends(get_db)):
    return logic.signup(db,details)

@app.delete('/deleteProfile',response_model=schemas.MessageResponse)
def deleteyouraccount(details:schemas.DeleteProfile, db:Session=Depends(get_db)):
    return logic.deleteprofile(db,details)


