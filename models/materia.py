from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Materia(Base):
    __tablename__ = 'materias'

    especialidad = Column(Integer, primary_key=True)
    plan = Column(Integer, primary_key=True)
    materia = Column(Integer, primary_key=True)
    nombre = Column(String(150), nullable=False)
    ano = Column(String(50), nullable=True)