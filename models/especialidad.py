from sqlalchemy import Column, Integer, String
from .base import Base

class Especialidad(Base):
  __tablename__ = 'especialidades'
  especialidad = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(100), nullable=False) 