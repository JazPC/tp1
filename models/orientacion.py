from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Orientacion(Base):
    __tablename__ = 'orientaciones'
    especialidad = Column(Integer, primary_key=True)
    plan = Column(Integer, primary_key=True)
    orientacion = Column(Integer, primary_key=True)
    nombre = Column(String(150), nullable=False)
