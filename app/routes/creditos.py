# Rutas para creditos
from flask import Blueprint
from app.models.creditos import Creditos

creditos = Blueprint('creditos', __name__, url_prefix='/creditos')


@creditos.route('/')
def indexCreditos():
    return "index"

@creditos.route('/add')
def addCredit():
    return "<h1>s</h1>"

@creditos.route('/list')
def listCredits():
    creditos = Creditos.query.all()
    return "a"

@creditos.route('/delete')
def deleteCredit():
    return "a"

@creditos.route('/edit')
def editCredit():
    return "a"



