"""stocks
id (PK)
product_id (FK)
estoque_atual
estoque_min
estoque_max
updated_at

stock_movments
id (PK)
product_id (FK)
tipo              -- ENTRADA / SAIDA
quantidade
origem            -- COMPRA / VENDA / AJUSTE
user_id (FK)
created_at

"""
from app.database import Base
from sqlalchemy import Column, Integer, Float, String, DateTime 
from datetime import datetime

class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_id = Column(Integer, nullable=False)  # Foreign Key to products table
    estoque_atual = Column(Float, nullable=False)
    estoque_min = Column(Float, nullable=False)
    estoque_max = Column(Float, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow)

class StockMovment(Base):
    __tablename__ = "stock_movments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_id = Column(Integer, nullable=False)  # Foreign Key to products table
    tipo = Column(String, nullable=False)  # ENTRADA / SAIDA
    quantidade = Column(Float, nullable=False)
    origem = Column(String, nullable=False)  # COMPRA / VENDA / AJUSTE
    user_id = Column(Integer, nullable=False)  # Foreign Key to users table
    created_at = Column(DateTime, default=datetime.utcnow)