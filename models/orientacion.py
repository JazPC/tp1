from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base

class Orientacion(Base):
  __tablename__ = 'orientacion'
  orientacion = Column(Integer, primary_key=True)
  especialidad = Column(Integer, ForeignKey('especialidades.especialidad'), nullable=False)
  plan = Column(Integer, ForeignKey('planes.plan'), nullable=False)
  nombre = Column(String(50), primary_key=True, nullable=False)