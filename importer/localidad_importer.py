from models.localidad import Localidad
from utils.xml_importer import import_data, with_session

@with_session
def importar_localidades(session, xml_path):
    import_data(session, xml_path, Localidad, record_tag='_exportar')

