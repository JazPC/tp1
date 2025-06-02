from models import Base
from db import engine
from importer.grado_importer import importar_grados
from importer.facultad_importer import importar_facultades

def main():
    print("Creando tablas...")
    Base.metadata.create_all(engine)

    importaciones = [
        (importar_grados, "xml/grados.xml"),
        (importar_facultades, "xml/facultades.xml"),
        # agregar acá los demás xml junto con sus rutas
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
