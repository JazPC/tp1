import unittest
import tempfile
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from utils.xml_importer import import_data
from models import Universidad

class TestImportUniversidad(unittest.TestCase):
    def setUp(self):
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)
        
        self.temp = tempfile.NamedTemporaryFile(delete=False, suffix=".xml", mode="w", encoding="Windows-1252")
        self.temp.write("""
        <root>
            <_expxml>
                <universida>1</universida>
		        <nombre>Universidad Nacional de Buenos Aires</nombre>
            </_expxml>
        </root>
        """)
        self.temp.close() 

    def tearDown(self):
        try:
            os.remove(self.temp.name)
        except Exception:
            pass

    def test_importar_Universidads(self):
        session = self.Session()
        import_data(session, self.temp.name, Universidad, record_tag="_expxml")
        session.commit()

        resultados = session.query(Universidad).order_by(Universidad.universida).all()
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0].universida, 1)
        self.assertEqual(resultados[0].nombre, "Universidad Nacional de Buenos Aires")


        session.close()

if __name__ == '__main__':
    unittest.main()
