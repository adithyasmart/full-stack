from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import hashlib

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    role = Column(Enum("receptionist", "doctor", name="user_roles"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def create_user(username: str, password: str):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return User(username=username, password_hash=hashed_password)

    def authenticate(user_input_password: str):
        return self.password_hash == hashlib.sha256(user_input_password.encode()).hexdigest()
