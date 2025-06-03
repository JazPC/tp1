from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base

class Materia(Base):
    __tablename__ = 'materias'
    materia = Column(Integer, primary_key=True)
    especialidad = Column(Integer, ForeignKey('especialidades.especialidad'), nullable=False)
    plan = Column(Integer, ForeignKey('planes.plan'), nullable=False)
    nombre = Column(String(100), nullable=False, unique=True)
    año = Column(Integer, nullable=False)