"""id (PK)
name
email
password_hash
role                -- admin / vendedor
is_active
created_at
"""





from app.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(ForeignKey("roles.id"), nullable=False)
    is_active = Column(Integer, default=1)  # 1 for active, 0 for inactive
    created_at = Column(DateTime, default=datetime.utcnow)
    