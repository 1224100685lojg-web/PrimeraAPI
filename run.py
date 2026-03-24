from app import create_app, db
from app.models.estudiante import Estudiante

# IMPORTAR MODELOS
from app.models.estudiante import Estudiante
from app.models.materia import Materia
from app.models.calificacion import Calificacion

app = create_app()

if __name__ == "__main__":

    with app.app_context():
        db.create_all()
        print("Tablas creadas correctamente")

    print("Servidor iniciado en http://localhost:5000")

    app.run(host="0.0.0.0", port=5000, debug=True)