from app.extensions import db

class Creditos(db.Model):
    """
    Representa un crédito otorgado a un cliente. 
    Hereda de la clase Model de SQLAlchemy para realizar la operaciones en la base de datos.

    Atributos:
        id (int)                 : Identificador del crédito.
        cliente (str)            : Nombre del cliente.
        monto (float)            : Monto del crédito.
        tasa_interes (float)     : Tasa de interés aplicada.
        plazo (int)              : Plazo en meses.
        fecha_otorgamiento (str) : Fecha en formato YYYY-MM-DD.
    """
    __tablename__ = 'creditos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cliente = db.Column(db.String(100), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    tasa_interes = db.Column(db.Float, nullable=False)
    plazo = db.Column(db.Integer, nullable=False)
    fecha_otorgamiento = db.Column(db.String(100), nullable=False)

    def __init__(self, cliente, monto, tasa_interes, plazo, fecha_otorgamiento):
        self.cliente = cliente
        self.monto = monto 
        self.tasa_interes = tasa_interes
        self.plazo = plazo
        self.fecha_otorgamiento = fecha_otorgamiento