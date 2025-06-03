from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base

class Orientacion(Base):
    __tablename__ = 'orientaciones'
    id = Column(Integer, primary_key=True, autoincrement=True) 
    orientacion = Column(Integer, nullable=False)
    especialidad = Column(Integer, ForeignKey('especialidades.especialidad'), nullable=False)
    plan = Column(Integer, ForeignKey('planes.plan'), nullable=False)
    nombre = Column(String(100), nullable=True)
