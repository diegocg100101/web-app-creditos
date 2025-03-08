# Rutas para index
from flask import Blueprint, render_template

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def index():
    """
    Devuelve la página principal con un mensaje de bienvenida.

    Retorna:
        - Renderiza la página principal con un mensaje de bienvenida y la barra de navegación.
    """
    return render_template("index.html")