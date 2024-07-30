from fastapi import APIRouter, HTTPException, Depends
from ..services import user_services
from ..schemas.login_schema import LoginRequest, LoginResponse
from ..utils.hash_password import decrypt_password
from ..utils.jwt_management import create_access_token
from sqlalchemy.orm import Session
from ..db.db import SessionLocal
from datetime import timedelta

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

login_router = APIRouter()

@login_router.post("/login", response_model=LoginResponse)
def login(login_request: LoginRequest, db: Session = Depends(get_db)):
    db_user = user_services.get_user_by_email(db, email=login_request.email)
    if db_user is None or not decrypt_password(login_request.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(data={"sub": db_user.email}, expires_delta=access_token_expires)
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "email": db_user.email,
        "user_id": db_user.id
    }