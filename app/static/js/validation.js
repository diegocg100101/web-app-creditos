document.getElementById('formulario').addEventListener("submit", function (event) {
    // Deshabilita el envío hasta que todo esté validado
    event.preventDefault();

    let valid = true; // Variable booleana para determinar si el formulario es válido.

    // Almacena los valores del formulario en variables.
    let nombre = document.getElementById('cliente').value;
    let monto = document.getElementById('monto').value;
    let tasa = document.getElementById('tasa').value;
    let plazo = document.getElementById('plazo').value;
    let fecha = document.getElementById('fecha').value;

    // Valida que el campo "nombre" no esté vacío
    if (nombre === '') {
        document.getElementById('nombreMensaje').textContent = "Ingrese el nombre";
        valid = false;
    }

    // Valida que el campo "monto" no esté vacío y no sea negativo.
    if (monto === '' || parseFloat(monto) < 0) {
        document.getElementById('montoMensaje').textContent = "Ingrese el monto";
        valid = false;
    }

    // Valida que el campo "tasa" no esté vacío y no sea negativo.
    if (tasa === '' || parseFloat(tasa) < 0) {
        document.getElementById('tasaMensaje').textContent = "Ingrese la tasa de interés";
        valid = false;
    }
    
    // Valida que el campo "plazo" no esté vacío y no sea negativo.
    if (plazo === '' || parseFloat(plazo) < 0) {
        document.getElementById('plazoMensaje').textContent = "Ingrese el plazo";
        valid = false;
    }
    
    // Valida que el campo "fecha" no esté vacío.
    if (fecha === '') {
        document.getElementById('fechaMensaje').textContent = "Ingrese la fecha";
        valid = false;
    }

    // Solo si la variable es true se podrá enviar el la petición a la API.
    if (valid) {
        this.submit();
    }
})

/**
 * Función para validar el campo "nombre" en cuanto existe un cambio.
 */
function nombreValid() {
    let nombre = document.getElementById('cliente').value;
    if (nombre === '') {
        document.getElementById('nombreMensaje').textContent = "Ingrese el nombre";
    } else {
        document.getElementById('nombreMensaje').textContent = "";
    }
}

/**
 * Función para validar el campo "monto" y mostrar un mensaje en cuanto existe un cambio.
 */
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

/**
 * Función para validar el campo "tasa" y mostrar un mensaje en cuanto existe un cambio.
 */
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

/**
 * Función para validar el campo "plazo" y mostrar un mensaje en cuanto existe un cambio.
 */
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

/**
 * Función para validar el campo "fecha" y mostrar un mensaje en cuanto existe un cambio.
 */
function fechaValid() {
    let fecha = document.getElementById('fecha').value;
    if (fecha === '') {
        document.getElementById('fechaMensaje').textContent = "Ingrese la fecha";
    } else {
        document.getElementById('fechaMensaje').textContent = "";
    }
}