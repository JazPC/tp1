import unittest
import tempfile
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from utils.xml_importer import import_data
from models import Grado

class TestImportGrados(unittest.TestCase):
    def setUp(self):
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

        self.temp = tempfile.NamedTemporaryFile(delete=False, suffix=".xml", mode="w", encoding="Windows-1252")
        self.temp.write("""
        <root>
            <_expxml>
                <grado>1</grado>
                <nombre>Administración</nombre>
            </_expxml>
            <_expxml>
                <grado>2</grado>
                <nombre>Adjunto</nombre>
            </_expxml>
        </root>
        """)
        self.temp.close()

    def tearDown(self):
        try:
            os.remove(self.temp.name)
        except Exception:
            pass

    def test_importar_grados(self):
        session = self.Session()
        import_data(session, self.temp.name, Grado, record_tag="_expxml")
        session.commit()

        resultados = session.query(Grado).order_by(Grado.grado).all()
        self.assertEqual(len(resultados), 2)
        self.assertEqual(resultados[0].grado, 1)
        self.assertEqual(resultados[0].nombre, "Administración")
        self.assertEqual(resultados[1].grado, 2)
        self.assertEqual(resultados[1].nombre, "Adjunto")

        session.close()

if __name__ == '__main__':
    unittest.main()
      