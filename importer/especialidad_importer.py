from models.especialidad import Especialidad
from utils.xml_importer import import_data, with_session

@with_session
def import_especialidades(session, xml_path):
    import_data(session, xml_path, Especialidad, record_tag='_expxml')


  

