from dataclasses import dataclass
from . import db

@dataclass(init=False, repr=True, eq=True)
class Materia(db.Model):
    __tablename__ = 'materias'
    materia : int = db.Column(db.Integer, primary_key=True)
    especialidad : int = db.Column(db.Integer, db.ForeignKey('especialidades.id'), nullable=False)
    plan : int = db.Column(db.Integer, db.ForeignKey('planes.id'), nullable=False)
    nombre : str = db.Column(db.String(100), nullable=False, unique=True)
    año : int = db.Column(db.Integer, nullable=False)