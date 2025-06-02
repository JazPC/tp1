from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Pais(db.Model):
    __tablename__ = 'pais'
    pais : int = db.Column(db.Integer, primary_key=True)
    nombre : str = db.Column(db.String(50), nullable=False, unique=True)
