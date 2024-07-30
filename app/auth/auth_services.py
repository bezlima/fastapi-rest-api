from sqlalchemy.orm import Session
from ..models import user_model
from ..utils.hash_password import decrypt_password

def verify_password(db: Session, email: str, password: str) -> bool:
    user = db.query(user_model.User).filter(user_model.User.email == email).first()
    if user:
        if decrypt_password(password, user.hashed_password):
            return True
    return False
