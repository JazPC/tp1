from dataclasses import dataclass
from datetime import date
from . import db


@dataclass(init=False, repr=True, eq=True)
class Plan(db.Model):
  __tablename__ = 'planes'
  plan : int = db.Column(db.Integer, primary_key=True)
  nombre : str = db.Column(db.String(50), nullable=False)  
  especialidad : int = db.Column(db.Integer, db.ForeignKey('especialidades.id'), nullable=False)
  
