from sqlalchemy import Column, Integer, String
from .base import Base

class Universidad(Base):
    __tablename__ = 'universidades'
    universida = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)

    