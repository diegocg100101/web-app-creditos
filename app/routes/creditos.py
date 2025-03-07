# Rutas para creditos
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.creditos import Creditos
from app.extensions import db

creditos = Blueprint('creditos', __name__, url_prefix='/creditos')


@creditos.route('/')
def indexCreditos():
    return "index"

@creditos.route('/add', methods=['GET', 'POST'])
def addCredit():
    if request.method == 'POST':
        try:
            cliente = request.form.get('cliente')
            monto = request.form.get('monto')
            tasa = request.form.get('tasa')
            plazo = request.form.get('plazo')
            fecha = request.form.get('fecha')

            credito = Creditos(cliente, monto, tasa, plazo, fecha)
            
            db.session.add(credito)
            db.session.commit()
            return redirect(url_for('creditos.listCredits'))
        except:
            print('Los campos están mal')
            return render_template('creditos/add.html')
    else:
        return render_template('creditos/add.html')

@creditos.route('/list', methods=['GET'])
def listCredits():
    data = Creditos.query.all()
    return render_template('creditos/list.html', creditos = data)

@creditos.route('/delete/<int:id>')
def deleteCredit(id):
    credito = Creditos.query.get_or_404(id)
    db.session.delete(credito)
    db.session.commit()
    return redirect(url_for('creditos.listCredits'))

@creditos.route('/edit/<int:id>', methods=['GET', 'POST'])
def editCredit(id):
    data = Creditos.query.get_or_404(id)
    if request.method == 'POST': 
        try:   
            data.cliente = request.form.get('cliente')
            data.monto = request.form.get('monto')
            data.tasa_interes = request.form.get('tasa')
            data.plazo = request.form.get('plazo')
            data.fecha_otorgamiento = request.form.get('fecha')

            db.session.commit()
            return redirect(url_for('creditos.listCredits'))
        except:
            return render_template('creditos/edit.html', credito=data)
    else:
        return render_template('creditos/edit.html', credito=data)
    
@creditos.route('/graph')
def graphCredits():
    data = Creditos.query.all()
    total = len(data)
    montoTotal = sum(credito.monto for credito in data)
    distribucionClientesMonto = {}
    distribucionClientesCantidad = {}

    for credito in data:
        if credito.cliente in distribucionClientesMonto:
            distribucionClientesMonto[credito.cliente] += credito.monto
            distribucionClientesCantidad[credito.cliente] += 1
        else:
            distribucionClientesMonto[credito.cliente] = credito.monto
            distribucionClientesCantidad[credito.cliente] = 1


    return render_template('creditos/graphs.html', total=total, monto=montoTotal, distribucion=distribucionClientesMonto, cantidad=distribucionClientesCantidad)



