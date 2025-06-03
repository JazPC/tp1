from models import Base
from db import engine
from importer.especialidad_importer import importar_especialidades
from importer.facultad_importer import importar_facultades
from importer.grado_importer import importar_grados
from importer.localidad_importer import importar_localidades
from importer.materia_importer import importar_materias
from importer.orientacion_importer import importar_orientaciones
from importer.pais_importer import importar_paises
from importer.plan_importer import importar_planes
from importer.universidad_importer import importar_universidades

def main():
    print("Creando tablas...")
    Base.metadata.create_all(engine)

    importaciones = [
        (importar_especialidades, "xml/especialidades.xml"),
        (importar_facultades, "xml/facultades.xml"),
        (importar_grados, "xml/grados.xml"),
        (importar_localidades, "xml/localidades.xml"),
        (importar_materias, "xml/materias.xml"),
        (importar_orientaciones, "xml/orientaciones.xml"),
        (importar_paises, "xml/paises.xml"),
        (importar_planes, "xml/planes.xml"),
        (importar_universidades, "xml/universidad.xml"),
    ]

    for func_importar, archivo_xml in importaciones:
        try:
            print(f"Importando {archivo_xml} ...")
            func_importar(archivo_xml)
        except Exception as e:
            print(f"Error al importar {archivo_xml}: {e}")

    print("Importación finalizada.")

if __name__ == "__main__":
    main()
