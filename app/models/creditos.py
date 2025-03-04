from app.extensions import db

class Creditos(db.Model):
    __tablename__ = 'creditos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cliente = db.Column(db.String(100), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    tasa_interes = db.Column(db.Float, nullable=False)
    plazo = db.Column(db.Integer, nullable=False)
    fecha_otorgamiento = db.Column(db.String(100), nullable=False)

    def __init__(self, cliente, monto, tasaInteres, plazo, fecha):
        self.cliente = cliente
        self.monto = monto 
        self.tasaInteres = tasaInteres
        self.plazo = plazo
        self.fecha = fecha