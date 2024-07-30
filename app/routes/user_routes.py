from fastapi import APIRouter, HTTPException, Depends
from ..schemas import user_schema
from ..services import user_services
from sqlalchemy.orm import Session
from ..db.db import SessionLocal
from ..dependencies.auth_dependencie import get_current_user

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

user_router = APIRouter()

@user_router.post("/users/", response_model=user_schema.User)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = user_services.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_services.create_user(db=db, user=user)

@user_router.get("/users/", response_model=list[user_schema.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_services.get_users(db, skip=skip, limit=limit)
    return users

@user_router.get("/users/{user_id}", response_model=user_schema.User)
def read_user(user_id: int, db: Session = Depends(get_db), current_user: user_schema.User = Depends(get_current_user)):
    db_user = user_services.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@user_router.put("/users/{user_id}/password", response_model=user_schema.User)
def update_password(user_id: int, password_update: user_schema.UserPasswordUpdate, db: Session = Depends(get_db)):
    db_user = user_services.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    updated_user = user_services.update_user_password(db, user_id=user_id, new_password=password_update.new_password)
    return updated_user

@user_router.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_services.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    success = user_services.delete_user(db, user_id=user_id)
    if not success:
        raise HTTPException(status_code=500, detail="Failed to delete user")
    return {"detail": "User deleted successfully"}