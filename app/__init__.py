from flask import Flask
from config import Config
from .routes.creditos import creditos
from .routes.main import main
from .extensions import db
from .models.creditos import Creditos

def create_app():
    """
    Función para configurar la aplicación y registrar Blueprints

    Returns:
        Flask instance : instancia de Flask con la configuración de la app
    """
    app = Flask(__name__)
    
    app.config.from_object(Config)

    app.register_blueprint(creditos)
    app.register_blueprint(main)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
    