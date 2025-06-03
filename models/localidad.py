from sqlalchemy import Column, Integer, String
from .base import Base

class Localidad(Base):
    __tablename__ = 'localidades'
    codigo = Column(Integer, primary_key=True)
    ciudad = Column(String(100), nullable=False, unique=True)
    provincia = Column(String(100), nullable=False)
    pais_del_c = Column(String(100), nullable=False) 