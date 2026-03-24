from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import DevelopmentConfig

db = SQLAlchemy()

def create_app(config=DevelopmentConfig):

    app = Flask(__name__)

    app.config.from_object(config)

    db.init_app(app)

    CORS(app)

    # 🔹 RUTA PRINCIPAL (LA QUE TE FALTABA)
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    # 🔹 ESTUDIANTES
    from app.routes.estudiante import estudiantes_bp
    app.register_blueprint(estudiantes_bp)
    
    # 🔹 CALIFICACIONES
    from app.routes.calificaciones import cal_bp
    app.register_blueprint(cal_bp)
    
    # 🔹 MATERIAS
    from app.routes.materias import materias_bp
    app.register_blueprint(materias_bp, url_prefix="/api/materias")
    
    # 🔹 JWT
    from flask_jwt_extended import JWTManager
    jwt = JWTManager()
    app.config["JWT_SECRET_KEY"] = "super-secret-key"
    jwt.init_app(app)
    
    # 🔹 AUTH
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    
    return app