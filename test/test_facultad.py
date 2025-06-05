import unittest
import tempfile
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from utils.xml_importer import import_data
from models import Facultad

class TestImportFacultades(unittest.TestCase):
    def setUp(self):
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

        self.temp = tempfile.NamedTemporaryFile(delete=False, suffix=".xml", mode="w", encoding="Windows-1252")
        self.temp.write("""
        <root>
            <_expxml>
                <facultad>1</facultad>
                <nombre>Facultad Regional Avellaneda</nombre>
            </_expxml>
            <_expxml>
                <facultad>2</facultad>
                <nombre>Facultad Regional Bahía Blanca</nombre>
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
        import_data(session, self.temp.name, Facultad, record_tag="_expxml")
        session.commit()

        resultados = session.query(Facultad).order_by(Facultad.facultad).all()
        self.assertEqual(len(resultados), 2)
        self.assertEqual(resultados[0].facultad, 1)
        self.assertEqual(resultados[0].nombre, "Facultad Regional Avellaneda")
        self.assertEqual(resultados[1].facultad, 2)
        self.assertEqual(resultados[1].nombre, "Facultad Regional Bahía Blanca")

        session.close()

if __name__ == '__main__':
    unittest.main()
      