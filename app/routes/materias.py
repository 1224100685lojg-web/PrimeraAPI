from flask import Blueprint, request, jsonify
from app import db
from app.models.materia import Materia

materias_bp = Blueprint("materias", __name__)

@materias_bp.route("/", methods=["POST"])
def crear_materia():
    data = request.get_json()

    nueva = Materia(
        clave=data["clave"],
        nombre=data["nombre"],
        creditos=data["creditos"],
        docente=data["docente"]
    )

    db.session.add(nueva)
    db.session.commit()

    return jsonify({
        "mensaje": "Materia creada",
        "id": nueva.id
    }), 201