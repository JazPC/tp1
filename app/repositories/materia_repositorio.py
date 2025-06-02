from app.models import Materia
from app import db


class MateriaRepository:

  @staticmethod
  def crear_materia(materia: Materia):
    db.session.add(materia)
    db.session.commit()
    return materia
  
