from app.models.pais import Pais
from app.repositories.pais_repositorio import PaisRepository

class PaisService:

  @staticmethod
  def crear_pais(pais: Pais):
    PaisRepository.crear_pais(pais)
    return pais
