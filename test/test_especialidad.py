from utils.xml_importer import import_data
from models import Especialidad
import tempfile
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
import unittest

class TestImportEspecialidades(unittest.TestCase):
    def setUp(self):
        # Crea base de datos en memoria y las tablas
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

    def test_importar_especialidades(self):
        # XML de prueba
        xml_content = """
        <root>
            <_expxml>
                <especialidad>1</especialidad>
                <nombre>Cardiología</nombre>
            </_expxml>
            <_expxml>
                <especialidad>2</especialidad>
                <nombre>Neurología</nombre>
            </_expxml>
        </root>
        """

        # Crea archivo temporal para simular el XML de entrada
        with tempfile.NamedTemporaryFile(delete=False, suffix=".xml", mode="w", encoding="Windows-1252") as temp:
            temp.write(xml_content)
            temp_path = temp.name

        session = self.Session()
        import_data(session, temp_path, Especialidad, record_tag="_expxml")
        session.commit()

        # Consultar datos importados
        resultados = session.query(Especialidad).order_by(Especialidad.especialidad).all()

        # Comprobar que se importaron 2 registros
        self.assertEqual(len(resultados), 2)
        # Validar contenido de cada registro
        self.assertEqual(resultados[0].especialidad, 1)
        self.assertEqual(resultados[0].nombre, "Cardiología")
        self.assertEqual(resultados[1].especialidad, 2)
        self.assertEqual(resultados[1].nombre, "Neurología")

        # Eliminar archivo temporal
        os.remove(temp_path)

if __name__ == '__main__':
    unittest.main()
