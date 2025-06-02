from models.facultad import Facultad
from utils.xml_importer import import_data, with_session

@with_session
def importar_facultades(session, xml_path):
    import_data(session, xml_path, Facultad, record_tag='_expxml')
