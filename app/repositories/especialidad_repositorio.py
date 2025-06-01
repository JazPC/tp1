from app.models import Especialidad
from app import db


class EspecialidadRepository:

  @staticmethod
  def crear_especialidad(especialidad: Especialidad):
    db.session.add(especialidad)
    db.session.commit()
    return facultad
  
