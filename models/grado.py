from sqlalchemy import Column, Integer, String
from .base import Base

class Grado(Base):
    __tablename__ = 'grados'
    grado = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
