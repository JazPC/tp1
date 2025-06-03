from sqlalchemy import Column, Integer, String
from .base import Base  

class Plan(Base):
  __tablename__ = 'planes'

  especialidad = Column(Integer, primary_key=True)  
  plan = Column(Integer, primary_key=True)          
  nombre = Column(String(150), nullable=True)
