from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import db
from app.models.usuario import Usuario
from datetime import timedelta

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/registro", methods=["POST"])
def registro():

    datos = request.get_json()

    if Usuario.query.filter_by(username=datos["username"]).first():
        return jsonify({"error": "El username ya está en uso"}), 409

    usuario = Usuario(
        username=datos["username"],
        email=datos["email"],
        rol=datos.get("rol", "docente")
    )

    usuario.set_password(datos["password"])

    db.session.add(usuario)
    db.session.commit()

    return jsonify({
        "mensaje": "Usuario creado",
        "id": usuario.id
    }), 201


@auth_bp.route("/login", methods=["POST"])
def login():

    datos = request.get_json()

    usuario = Usuario.query.filter_by(username=datos["username"]).first()

    if not usuario or not usuario.check_password(datos["password"]):
        return jsonify({"error": "Credenciales inválidas"}), 401

    token = create_access_token(
        identity={"id": usuario.id, "rol": usuario.rol},
        expires_delta=timedelta(hours=24)
    )

    return jsonify({
        "token": token,
        "tipo": "Bearer",
        "expira_en": "24 horas"
    }), 200


@auth_bp.route("/perfil", methods=["GET"])
@jwt_required()
def perfil():

    identidad = get_jwt_identity()

    usuario = Usuario.query.get(identidad["id"])

    return jsonify({
        "usuario": usuario.username,
        "rol": identidad["rol"]
    }), 200