from app.services.especialidad_service import importar_especialidades
from app.config.config import Base, engine

if __name__ == "__main__":
    # Crear las tablas si no existen
    Base.metadata.create_all(bind=engine)

    # Importar XML
    importar_especialidades()
    print("Importación completada.")
