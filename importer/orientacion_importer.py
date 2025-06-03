from models.orientacion import Orientacion
from utils.xml_importer import import_data, with_session

@with_session
def import_orientaciones(session, xml_path):
    import_data(session, xml_path, Orientacion, record_tag='_expxml')

