from dataclasses import dataclass
#from app.models.relaciones import materias_planes # del chat, ver porque el profe usó users_roles
from app import db

@dataclass(init=False, repr=True, eq=True)
class Materia:#(db.Model)
    #__tablename__ = 'materias'
    #autoridades = db.relationship('Autoridad', secondary='autoridades_materias', back_populates='materias')
    nombre: str
    diseno_curricular: str
    correlativas: list
    horas_dictadas: str
    promocional: bool
    nivel: str
    
    orientacion = db.relationship('Orientacion')
    
    autoridades = db.relationship('Autoridad', secondary='autoridades_materias', backref='materias')
    
    def asociar_autoridad(self, autoridad):
        if autoridad not in self.autoridades:
            self.autoridades.append(autoridad)
            
    def desasociar_autoridad(self, autoridad):
        if autoridad in self.autoridades:
            self.autoridades.remove(autoridad)
    
    