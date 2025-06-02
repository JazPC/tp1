from app.models import Grado
from app.repositories.grado_repositorio import GradoRepository

class GradoService:

  @staticmethod
  def crear_grado(grado: Grado):
    GradoRepository.crear_grado(grado)
    return grado
