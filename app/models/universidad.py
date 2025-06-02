from dataclasses import dataclass

@dataclass(init=False, repr=True, eq=True)
class Universidad(db.Model):
    __tablename__ = 'universidades'
    universida : int = db.Column(db.Integer, primary_key=True)
    nombre : str = db.Column(db.String(100), nullable=False)

    