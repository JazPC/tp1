import time

from models import Base
from db import engine
from importer.especialidad_importer import import_especialidades
from importer.facultad_importer import import_facultades
from importer.grado_importer import import_grados
from importer.localidad_importer import import_localidades
from importer.materia_importer import import_materias
from importer.orientacion_importer import import_orientaciones
from importer.pais_importer import import_paises
from importer.plan_importer import import_planes
from importer.universidad_importer import import_universidades


def main():
    print("Creando tablas...")
    Base.metadata.create_all(engine)


    imports = [
        (import_especialidades, "xml/especialidades.xml"),
        (import_facultades, "xml/facultades.xml"),
        (import_grados, "xml/grados.xml"),
        (import_localidades, "xml/localidades.xml"),
        (import_orientaciones, "xml/orientaciones.xml"),
        (import_paises, "xml/paises.xml"),
        (import_planes, "xml/planes.xml"),
        (import_materias, "xml/materias.xml"),
        (import_universidades, "xml/universidades.xml"),
    ]

    start_total = time.time()

    for func_import, xml_file in imports:
        try:
            print(f"Importando {xml_file} ...")
            start = time.time()
            func_import(xml_file)
            end = time.time()
            print(f"Importado {xml_file} en {end - start:.2f} segundos.")
        except Exception as e:
            print(f"Error al importar {xml_file}: {e}")

    end_total = time.time()
    print(f"Importación finalizada en {end_total - start_total:.2f} segundos.")

if __name__ == "__main__":
    main()
