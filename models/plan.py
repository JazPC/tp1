from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base  

class Plan(Base):
  __tablename__ = 'planes'
  plan = Column(Integer, primary_key=True)
  nombre = Column(String(50), nullable=True)  
  especialidad = Column(Integer, ForeignKey('especialidades.especialidad'), nullable=False)
  
