"""id (PK)
razao_social
nome_fantasia
cnpj
inscricao_estadual
regime_tributario     -- simples / presumido / real
endereco
municipio
uf
"""
from app.database import Base
from sqlalchemy import Column, Integer, String
from datetime import datetime