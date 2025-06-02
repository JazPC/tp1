from models.grado import Grado
from utils.xml_importer import import_data, with_session

@with_session
def importar_grados(session, xml_path):
    import_data(session, xml_path, Grado, record_tag='_expxml')
