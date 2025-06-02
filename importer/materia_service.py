from app.models import Materia
from app.repositories.materia_repositorio import MateriaRepository

class MateriaService:

  @staticmethod
  def crear_materia(materia: Materia):
    MateriaRepository.crear_materia(materia)
    return materia
