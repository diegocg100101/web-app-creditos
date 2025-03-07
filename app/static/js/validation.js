document.getElementById('formulario').addEventListener("submit", function (event) {
    // Deshabilita el envío hasta que todo esté validado
    event.preventDefault();

    let valid = true;

    let nombre = document.getElementById('cliente').value;
    let monto = document.getElementById('monto').value;
    let tasa = document.getElementById('tasa').value;
    let plazo = document.getElementById('plazo').value;
    let fecha = document.getElementById('fecha').value;

    if (nombre === '') {
        document.getElementById('nombreMensaje').textContent = "Ingrese el nombre";
        valid = false;
    }

    if (monto === '' || parseFloat(monto) < 0) {
        document.getElementById('montoMensaje').textContent = "Ingrese el monto";
        valid = false;
    }

    if (tasa === '' || parseFloat(tasa) < 0) {
        document.getElementById('tasaMensaje').textContent = "Ingrese la tasa de interés";
        valid = false;
    }

    if (plazo === '' || parseFloat(plazo) < 0) {
        document.getElementById('plazoMensaje').textContent = "Ingrese el plazo";
        valid = false;
    }

    if (fecha === '') {
        document.getElementById('fechaMensaje').textContent = "Ingrese la fecha";
        valid = false;
    }

    if (valid) {
        this.submit();
    }
})

function nombreValid() {
    let nombre = document.getElementById('cliente').value;
    if (nombre === '') {
        document.getElementById('nombreMensaje').textContent = "Ingrese el nombre";
    } else {
        document.getElementById('nombreMensaje').textContent = "";
    }
}

function montoValid() {
    let monto = document.getElementById('monto').value;
    if (monto === '') {
        document.getElementById('montoMensaje').textContent = "Ingrese el monto";
    } else if (parseFloat(monto) < 0) {
        document.getElementById('montoMensaje').textContent = "El monto no puede ser negativo";
    } else {
        document.getElementById('montoMensaje').textContent = "";
    }
}

function tasaValid() {
    let tasa = document.getElementById('tasa').value;
    if (tasa === '') {
        document.getElementById('tasaMensaje').textContent = "Ingrese la tasa de interés";
    } else if (parseFloat(tasa) < 0) {
        document.getElementById('tasaMensaje').textContent = "La tasa no puede ser negativa";
    } else {
        document.getElementById('tasaMensaje').textContent = "";
    }
}


function plazoValid() {
    let plazo = document.getElementById('plazo').value;
    if (plazo === '') {
        document.getElementById('plazoMensaje').textContent = "Ingrese el plazo";
    } else if (parseFloat(plazo) < 0) {
        document.getElementById('plazoMensaje').textContent = "El plazo no puede ser negativo";
    } else {
        document.getElementById('plazoMensaje').textContent = "";
    }
}

function fechaValid() {
    let fecha = document.getElementById('fecha').value;
    if (fecha === '') {
        document.getElementById('fechaMensaje').textContent = "Ingrese la fecha";
    } else {
        document.getElementById('fechaMensaje').textContent = "";
    }
}