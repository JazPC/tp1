from app.models import Localidad
from app import db


class LocalidadRepository:

  @staticmethod
  def crear_localidad(localidad: Localidad):
    db.session.add(localidad)
    db.session.commit()
    return localidad
  
