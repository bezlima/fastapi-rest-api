from sqlalchemy.orm import Session
from ..models import user_model
from ..schemas import user_schema
from ..utils.hash_password import encrypt_password

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_model.User).offset(skip).limit(limit).all()

def get_user(db: Session, user_id: int):
    return db.query(user_model.User).filter(user_model.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(user_model.User).filter(user_model.User.email == email).first()

def delete_user(db: Session, user_id: int):
    user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False

def update_user_password(db: Session, user_id: int, new_password: str):
    user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if user:
        hashed_password = encrypt_password(new_password)
        user.hashed_password = hashed_password
        db.commit()
        db.refresh(user)
        return user
    return None

def create_user(db: Session, user: user_schema.UserCreate):
    hashed_password = encrypt_password(user.password)
    db_user = user_model.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user