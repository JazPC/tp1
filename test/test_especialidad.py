import unittest
import tempfile
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from utils.xml_importer import import_data
from models import Especialidad

class TestImportEspecialidades(unittest.TestCase):
    def setUp(self):
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

        self.temp = tempfile.NamedTemporaryFile(delete=False, suffix=".xml", mode="w", encoding="Windows-1252")
        self.temp.write("""
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
        """)
        self.temp.close()

    def tearDown(self):
        try:
            os.remove(self.temp.name)
        except Exception:
            pass

    def test_importar_especialidades(self):
        session = self.Session()
        import_data(session, self.temp.name, Especialidad, record_tag="_expxml")
        session.commit()

        resultados = session.query(Especialidad).order_by(Especialidad.especialidad).all()
        self.assertEqual(len(resultados), 2)
        self.assertEqual(resultados[0].especialidad, 1)
        self.assertEqual(resultados[0].nombre, "Cardiología")
        self.assertEqual(resultados[1].especialidad, 2)
        self.assertEqual(resultados[1].nombre, "Neurología")

        session.close()

if __name__ == '__main__':
    unittest.main()
      