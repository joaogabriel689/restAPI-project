import hashlib

from models.usermodels import User

def hash_password(password: str) -> str:
    password_bytes = password.encode('utf-8')
    password_hash = hashlib.sha256(password_bytes)
    return password_hash.hexdigest()

def verify_password(password: str, hashed_password: str) -> bool:
    password_hash = hash_password(password)
    return password_hash == hashed_password

def verify_user(email: str, db) -> bool:
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return False
    return True