from models.universidad import Universidad
from utils.xml_importer import import_data, with_session

@with_session
def import_universidades(session, xml_path):
    import_data(session, xml_path, Universidad, record_tag='_expxml')

