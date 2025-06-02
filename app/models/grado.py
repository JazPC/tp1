from dataclasses import dataclass
from grado import db

@dataclass(init=False, repr=True, eq=True)
class Grado(db.Model):
  __tablename__ = 'grados'
  grado : int = db.Column(db.Integer, primary_key=True)
  nombre : str = db.Column(db.String(100), nullable=False, unique=True)  
  