import xml.etree.ElementTree as ET
from app.models.localidad import Localidad
from app.repositories.localidad_repositorio import LocalidadRepository

class LocalidadService:
    
    @staticmethod
    def crear_localidad(localidad: Localidad):
        LocalidadRepository.crear_localidad(localidad)
        return localidad
    @staticmethod
    def cargar_desde_xml(path_xml: str):
        tree = ET.parse(path_xml)
        root = tree.getroot()

        for elem in root.findall('exportar'):
            ciudad = elem.find('ciudad').text
            provincia = elem.find('provincia').text
            pais = elem.find('pais_del_c').text

            nueva_localidad = Localidad(
                ciudad=ciudad,
                provincia=provincia,
                pais_del_c=pais
            )
            LocalidadService.crear_localidad(nueva_localidad)
