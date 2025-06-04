from models.materia import Materia
from utils.xml_importer import import_data, with_session

@with_session
def import_materias(session, xml_path):
    import_data(session, xml_path, Materia, record_tag='_expxml')
