
"""
tributation
id (PK)
descricao
icms_cst
icms_aliquota
icms_base_reducao
pis_cst
pis_aliquota
cofins_cst
cofins_aliquota
ipi_cst
ipi_aliquota
created_at

NF
id (PK)
sale_id (FK)
numero
serie
chave_acesso
modelo                -- 55 / 65
total_produtos
total_impostos
total_nota
status                -- EMITIDA / CANCELADA
emitida_em

"""

from app.database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

class Tributation(Base):
    __tablename__ = "tributation"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    descricao = Column(String, nullable=False)
    icms_cst = Column(String, nullable=False)
    icms_aliquota = Column(Float, nullable=False)
    icms_base_reducao = Column(Float, nullable=True)
    pis_cst = Column(String, nullable=False)
    pis_aliquota = Column(Float, nullable=False)
    cofins_cst = Column(String, nullable=False)
    cofins_aliquota = Column(Float, nullable=False)
    ipi_cst = Column(String, nullable=False)
    ipi_aliquota = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class NF(Base):
    __tablename__ = "nf"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sale_id = Column(Integer, nullable=False)  # Foreign Key to sales table
    numero = Column(String, nullable=False)
    serie = Column(String, nullable=False)
    chave_acesso = Column(String, unique=True, nullable=False)
    modelo = Column(String, nullable=False)  # 55 / 65
    total_produtos = Column(Float, nullable=False)
    total_impostos = Column(Float, nullable=False)
    total_nota = Column(Float, nullable=False)
    status = Column(String, nullable=False)  # EMITIDA / CANCELADA
    emitida_em = Column(DateTime, default=datetime.utcnow)