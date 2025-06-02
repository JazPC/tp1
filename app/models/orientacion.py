from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Orientacion(db.Model):
  __tablename__ = 'orientacion'
  orientacion : int = db.Column(db.Integer, primary_key=True)
  especialidad : int = db.Column(db.Integer, foreign_key='especialidad.id', nullable=False)
  plan : int = db.Column(db.Integer, foreign_key='plan.id', nullable=False)
  nombre : str = db.Column(db.String(50), primary_key=True, nullable=False)