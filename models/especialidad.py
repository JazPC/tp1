from sqlalchemy import Column, Integer, String
from .base import Base

class Especialidad(Base):
  __tablename__ = 'especialidades'

  especialidad = Column(Integer, primary_key=True)
  nombre = Column(String(150), nullable=False)
