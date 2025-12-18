"""
sales

id (PK)
user_id (FK)          -- vendedor
subtotal
total_impostos
total_geral
status                -- OPEN / FINALIZED / CANCELED
created_at

snapshot_sales
id (PK)
sale_id (FK)
product_id (FK)

-- snapshot do produto
product_name
ean_gtin
ncm
cest

quantidade
preco_unitario

-- impostos congelados
icms_cst
icms_aliquota
icms_valor

pis_cst
pis_aliquota
pis_valor

cofins_cst
cofins_aliquota
cofins_valor

ipi_cst
ipi_aliquota
ipi_valor

total_item

"""

from app.database import Base
from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)  # Foreign Key to users table
    subtotal = Column(Float, nullable=False)
    total_impostos = Column(Float, nullable=False)
    total_geral = Column(Float, nullable=False)
    status = Column(String, nullable=False)  # OPEN / FINALIZED / CANCELED
    created_at = Column(DateTime, default=datetime.utcnow)

class SnapshotSale(Base):
    __tablename__ = "snapshot_sales"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sale_id = Column(Integer, nullable=False)  # Foreign Key to sales table
    product_id = Column(Integer, nullable=False)  # Foreign Key to products table

    # Snapshot do produto
    product_name = Column(String, nullable=False)
    ean_gtin = Column(String, nullable=False)
    ncm = Column(String, nullable=False)
    cest = Column(String, nullable=True)

    quantidade = Column(Float, nullable=False)
    preco_unitario = Column(Float, nullable=False)

    # Impostos congelados
    icms_cst = Column(String, nullable=False)
    icms_aliquota = Column(Float, nullable=False)
    icms_valor = Column(Float, nullable=False)

    pis_cst = Column(String, nullable=False)
    pis_aliquota = Column(Float, nullable=False)
    pis_valor = Column(Float, nullable=False)

    cofins_cst = Column(String, nullable=False)
    cofins_aliquota = Column(Float, nullable=False)
    cofins_valor = Column(Float, nullable=False)

    ipi_cst = Column(String, nullable=False)
    ipi_aliquota = Column(Float, nullable=False)
    ipi_valor = Column(Float, nullable=False)

    total_item = Column(Float, nullable=False)