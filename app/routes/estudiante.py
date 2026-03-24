# app/routes/estudiantes.py
from flask import Blueprint, jsonify, request
from app import db
from app.models.estudiante import Estudiante


estudiantes_bp = Blueprint('estudiantes', __name__, url_prefix='/api/estudiantes')


# ─────── CREATE: POST /api/estudiantes ────────────────────────────────
@estudiantes_bp.route("/", methods=["POST"])
def crear_estudiante():
    """
    Crea un nuevo estudiante.
    El cliente envía los datos en el cuerpo de la petición (JSON).
    Retorna el estudiante creado con código 201 (Created).
    """
    # Obtener datos del cuerpo JSON de la petición
    datos = request.get_json()
    
    # Validar que se enviaron datos
    if not datos:
        return jsonify({"error": "No se enviaron datos"}), 400
    
    # Validar campos requeridos
    campos_requeridos = ["matricula", "nombre", "apellido", "email", "carrera"]
    for campo in campos_requeridos:
        if campo not in datos:
            return jsonify({"error": f"El campo {campo} es requerido"}), 400
    
    # Verificar que la matrícula no exista ya
    if Estudiante.query.filter_by(matricula=datos["matricula"]).first():
        return jsonify({"error": "La matrícula ya está registrada"}), 409
    
    # Crear el objeto Estudiante
    nuevo = Estudiante(
        matricula=datos["matricula"],
        nombre=datos["nombre"],
        apellido=datos["apellido"],
        email=datos["email"],
        carrera=datos["carrera"],
        semestre=datos.get("semestre", 1)  # Valor por defecto: 1
    )
    
    # Guardar en la base de datos
    db.session.add(nuevo)
    db.session.commit()
    
    return jsonify({
        "mensaje": "Estudiante creado exitosamente",
        "estudiante": nuevo.to_dict()
    }), 201


# ─────── READ ALL: GET /api/estudiantes ──────────────────────────────
@estudiantes_bp.route("/", methods=["GET"])
def obtener_estudiantes():
    """
    Obtiene la lista de todos los estudiantes.
    Soporta filtros por carrera: GET /api/estudiantes?carrera=ITIC
    Soporta paginación: GET /api/estudiantes?pagina=1&por_pagina=10
    """
    # Parámetros de query string (opcionales)
    carrera = request.args.get("carrera")      # Filtro
    pagina = request.args.get("pagina", 1, type=int)
    por_pagina = request.args.get("por_pagina", 10, type=int)
    
    # Construir la consulta
    query = Estudiante.query.filter_by(activo=True)
    if carrera:
        query = query.filter_by(carrera=carrera)
    
    # Paginar los resultados
    paginacion = query.paginate(page=pagina, per_page=por_pagina)
    
    return jsonify({
        "total": paginacion.total,
        "paginas": paginacion.pages,
        "pagina_actual": pagina,
        "por_pagina": por_pagina,
        "estudiantes": [e.to_dict() for e in paginacion.items]
    }), 200


# ─────── READ ONE: GET /api/estudiantes/<id> ──────────────────────────
@estudiantes_bp.route("/<int:id>", methods=["GET"])
def obtener_estudiante(id):
    """Obtiene un estudiante por su ID."""
    # get_or_404: busca por PK; si no existe, retorna error 404 automáticamente
    estudiante = Estudiante.query.get_or_404(id, description="Estudiante no encontrado")
    return jsonify(estudiante.to_dict()), 200


# ─────── UPDATE: PUT /api/estudiantes/<id> ────────────────────────────
@estudiantes_bp.route("/<int:id>", methods=["PUT"])
def actualizar_estudiante(id):
    """Actualiza los datos de un estudiante existente."""
    estudiante = Estudiante.query.get_or_404(id)
    datos = request.get_json()
    
    # Actualizar solo los campos que se enviaron
    if "nombre" in datos:
        estudiante.nombre = datos["nombre"]
    if "apellido" in datos:
        estudiante.apellido = datos["apellido"]
    if "email" in datos:
        estudiante.email = datos["email"]
    if "carrera" in datos:
        estudiante.carrera = datos["carrera"]
    if "semestre" in datos:
        estudiante.semestre = datos["semestre"]
    
    db.session.commit()
    return jsonify({"mensaje": "Actualizado", "estudiante": estudiante.to_dict()}), 200


# ─────── DELETE: DELETE /api/estudiantes/<id> ─────────────────────────
@estudiantes_bp.route("/<int:id>", methods=["DELETE"])
def eliminar_estudiante(id):
    """
    Eliminación LÓGICA: no borra el registro, solo lo marca como inactivo.
    Esto es una buena práctica: nunca pierdas datos de manera permanente.
    """
    estudiante = Estudiante.query.get_or_404(id)
    estudiante.activo = False  # Borrado lógico
    db.session.commit()
    return jsonify({"mensaje": f"Estudiante {estudiante.matricula} desactivado"}), 200

