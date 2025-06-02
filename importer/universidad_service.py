from app.models import Universidad
from app.repositories.universidad_repositorio import UniversidadRepository

class UniversidadService:

  @staticmethod
  def crear_universidad(universidad: Universidad):
    UniversidadRepository.crear_universidad(universidad)
    return universidad
