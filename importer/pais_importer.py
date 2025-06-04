from models.pais import Pais
from utils.xml_importer import import_data, with_session

@with_session
def import_paises(session, xml_path):
    import_data(session, xml_path, Pais, record_tag='_expxml')
