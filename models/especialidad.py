from dataclasses import dataclass
from . import db
@dataclass(init=False, repr=True, eq=True)
class Especialidad(db.Model):
  __tablename__ = 'especialidades'
  especialidad : int = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nombre : str = db.Column(db.String(100), nullable=False, unique=True) 