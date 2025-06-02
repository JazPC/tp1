import xml.etree.ElementTree as ET
from app.models import Facultad
from app.repositories.facultad_repositorio import FacultadRepository

class FacultadService:
  
  @staticmethod
  def crear_facultad(facultad: Facultad):
    FacultadRepository.crear_facultad(facultad)
    return facultad
  
  
  @staticmethod
  def cargar_desde_xml(path_xml: str):
    tree = ET.parse(path_xml)
    root = tree.getroot()

    for elem in root.findall('exportar'):
      facultad = elem.find('facultad').text
      nombre = elem.find('nombre').text

      nueva_facultad = Facultad(
        facultad=facultad,
        nombre=nombre
      )
      FacultadService.crear_facultad(nueva_facultad)
    