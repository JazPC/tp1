from sqlalchemy import Column, Integer, String
from .base import Base

class Pais(Base):
    __tablename__ = 'pais'
    pais = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False, unique=True)
