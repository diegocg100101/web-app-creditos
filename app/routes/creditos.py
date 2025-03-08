# Rutas para creditos
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.creditos import Creditos
from app.extensions import db

creditos = Blueprint('creditos', __name__, url_prefix='/creditos')


@creditos.route('/add', methods=['GET', 'POST'])
def addCredit():
    """
    Agrega un nuevo crédito a la base de datos.

    Métodos:
        - GET  : Muestra el formulario de registro.
        - POST : Recibe los datos del formulario y crea un nuevo crédito en la base de datos.

    Parámetros en request.form:
        - cliente (str) : Nombre del cliente.
        - monto (float) : Monto del crédito.
        - tasa (float)  : Tasa de interés aplicada.
        - plazo (int)   : Plazo en meses.
        - fecha (str)   : Fecha de otorgamiento (YYYY-MM-DD).

    Retorna:
        - Redirige a la lista de créditos si la operación es exitosa.
        - Si la operación no es exitosa, renderiza nuevamente el formulario.
        - Renderiza el formulario con un mensaje de error si falla la operación.
    """
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
            return render_template('creditos/add.html')
    else:
        return render_template('creditos/add.html')

@creditos.route('/list')
def listCredits():
    """
    Devuelve todos los créditos ingresados en la base de datos.

    Retorna:
        - Renderiza la tabla con la lista de créditos obtenidos de la base de datos.
    """
    data = Creditos.query.all()
    return render_template('creditos/list.html', creditos = data)

@creditos.route('/delete/<int:id>')
def deleteCredit(id):
    """
    Elimina el crédito correspondiente al ID en la base de datos. 

    Parámetros:
        - id (int) : ID del crédito a eliminar.

    Flujo:
        - Busca el crédito por el ID en la base de datos.
        - Si el crédito existe, lo elimina de la base de datos.
        - Si el crédito no existe, devuelve un error 404.

    Retorna:
        - Redirige a la lista de créditos si todo es exitoso.
    """
    credito = Creditos.query.get_or_404(id)
    db.session.delete(credito)
    db.session.commit()
    return redirect(url_for('creditos.listCredits'))

@creditos.route('/edit/<int:id>', methods=['GET', 'POST'])
def editCredit(id):
    """
    Edita los datos de un crédito existente en la base de datos.

    Métodos:
        - GET  : Muestra el formulario de edición con los valores del crédito correspondiente al ID.
        - POST : Actualiza los datos del crédito en la base de datos.

    Parámetros en request.form:
        - cliente (str) : Nombre del cliente.
        - monto (float) : Monto del crédito.
        - tasa (float)  : Tasa de interés aplicada.
        - plazo (int)   : Plazo en meses.
        - fecha (str)   : Fecha de otorgamiento (YYYY-MM-DD).

    Parámetro en URL:
        - id (in) : ID del crédito a editar.

    Flujo:
        - Busca el crédito por el ID en la base de datos.
        - Si el crédito existe, modifica los atributos de la instancia y lo almacena en la base de datos.
        - Si el crédito no existe, devuelve un error 404.

    Retorna:
        - Redirige a la lista de créditos si la operación es exitosa.
        - Renderiza el formulario y devuelve un error 404.
        - Renderiza el formulario de edición con los valores del crédito correspondiente al ID.
    """
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
    """
    Devuelve la información necesaria para graficar el total de créditos otorgados, el monto total,
    la distribución de monto de cada cliente y la distribución de créditos otorgados de cada cliente.

    Flujo:
        - Obtiene todos los créditos de la base de datos.
        - Almacena el total de instancias devueltas de la base de datos.
        - Suma y almacena el monto total de todos los créditos otorgados.
        - Crea dos diccionarios: uno almacena la suma del monto total por cliente y el otro almacena la cantidad de créditos otorgados por cliente.

    Retorna:
        - Renderiza las gráficas con la información de obtenida de la base de datos.
    """
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



