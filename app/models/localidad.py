from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Localidad(db.Model):
    __tablename__ = 'localidades'
    codigo : int = db.Column(db.Integer, primary_key=True)
    ciudad : str = db.Column(db.String(100), nullable=False, unique=True)
    provincia : str = db.Column(db.String(100), nullable=False)
    pais_del_c : str = db.Column(db.String(100), nullable=False) 