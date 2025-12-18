"""
id (PK)
nome
codigo                -- código interno
codigo_ref
codigo_extra
ean_gtin              -- código de barras (EAN / GTIN)
marca
categoria
sub_categoria
unidade
preco_base
peso_liquido
peso_bruto
ncm                   -- obrigatório fiscal
cest
tax_profile_id (FK)
fornecedor_principal
localizacao
status                -- ativo / inativo
kit_combo             -- boolean
imagem
created_at
updated_at
updated_by

"""

from app.database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from datetime import datetime

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    codigo = Column(String, unique=True, nullable=False)
    codigo_ref = Column(String, nullable=True)
    codigo_extra = Column(String, nullable=True)
    ean_gtin = Column(String, unique=True, nullable=True)
    marca = Column(String, nullable=True)
    categoria = Column(String, nullable=True)
    sub_categoria = Column(String, nullable=True)
    unidade = Column(String, nullable=False)
    preco_base = Column(Float, nullable=False)
    peso_liquido = Column(Float, nullable=True)
    peso_bruto = Column(Float, nullable=True)
    ncm = Column(String, nullable=False)
    cest = Column(String, nullable=True)
    tax_profile_id = Column(Integer, nullable=True)  # Foreign Key to tax_profiles table
    fornecedor_principal = Column(String, nullable=True)
    localizacao = Column(String, nullable=True)
    status = Column(String, nullable=False)  # ativo / inativo
    kit_combo = Column(Boolean, default=False)
    imagem = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    updated_by = Column(Integer, nullable=True)  # User ID who last updated the product