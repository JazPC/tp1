import xml.etree.ElementTree as ET
from app.models import Especialidad
from app.repositories.especialidad_repositorio import EspecialidadRepository

class EspecialidadService:

  @staticmethod
  def crear_especialidad(especialidad: Especialidad):
    EspecialidadRepository.crear_especialidad(especialidad)
    return especialidad

  @staticmethod
  def cargar_desde_xml(path_xml: str):
    tree = ET.parse(path_xml)
    root = tree.getroot()

    for elem in root.findall('exportar'):
      especialidad = elem.find('especialidad').text
      nombre = elem.find('nombre').text

      nueva_especialidad = Especialidad(
        especialidad=especialidad,
        nombre=nombre
      )
      EspecialidadService.crear_especialidad(nueva_especialidad)

  

