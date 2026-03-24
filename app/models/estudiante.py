from app import db
from datetime import datetime

class Estudiante(db.Model):

    __tablename__ = 'estudiantes'

    id = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.String(20), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    carrera = db.Column(db.String(100), nullable=False)
    semestre = db.Column(db.Integer, nullable=False, default=1)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    activo = db.Column(db.Boolean, default=True)
    calificaciones = db.relationship("Calificacion", back_populates="estudiante")


    def to_dict(self):
        return {
            "id": self.id,
            "matricula": self.matricula,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "carrera": self.carrera,
            "semestre": self.semestre,
            "activo": self.activo
        }