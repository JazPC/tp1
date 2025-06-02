from app.models import Universidad
from app import db


class UniversidadRepository:

  @staticmethod
  def crear_universidad(universidad: Universidad):
    db.session.add(universidad)
    db.session.commit()
    return universidad
  
