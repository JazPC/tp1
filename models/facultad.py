from sqlalchemy import Column, Integer, String
from .base import Base

class Facultad(Base):
    __tablename__ = 'facultades'
    facultad = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)