"""id (PK)
user_id (FK)
acao
entidade
entidade_id
dados_anteriores
dados_novos
created_at
"""
from app.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)  # Foreign Key to users table
    acao = Column(String, nullable=False)
    entidade = Column(String, nullable=False)
    entidade_id = Column(Integer, nullable=False)
    dados_anteriores = Column(Text, nullable=True)
    dados_novos = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)