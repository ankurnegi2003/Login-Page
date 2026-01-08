from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException

def findprofile(db:Session,email:str):
    """Helper function to fetch user by email"""
    return db.query(models.Profile).filter(models.Profile.email==email).first()

def signup(db:Session,details:schemas.Signup):
    # ########password encryption pending
    if findprofile(db, details.email):
        raise HTTPException(status_code=409, detail="Email already registered")
    user = models.Profile(
        name = details.name,
        dob = details.dob,
        email = details.email,
        password = details.password
    )
    #add rollback feature using try and catch
    # db.add(user)
    # db.commit()
    # db.refresh(user)
    # return user
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except:
        db.rollback()
        raise

#this shit leaking data, fix this
def signin(db:Session,details:schemas.Signin):
      # ########password encryption pending
    user = findprofile(db,details.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.password!=details.password:
        raise HTTPException(status_code=401, detail="Incorrect password")
    return user
#this shit also leaking data, fix this
def deleteprofile(db:Session,details:schemas.DeleteProfile):
    user = findprofile(db, details.email)
    # if not user:
    #     raise HTTPException(status_code=404, detail="Some error occured")
    if not user or user.password != details.password:
        raise HTTPException(status_code=401, detail="Some error occured")

    db.delete(user)
    db.commit()
    return {"detail": "User deleted successfully"}
    


