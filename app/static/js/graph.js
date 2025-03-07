const totalGraph = document.getElementById('graph-total');

console.log(cantidad)

new Chart(totalGraph, {
    type: 'bar',
    data: {
        labels: ['Cantidad de créditos otorgados'],
        datasets: [{
            label: 'Cantidad de créditos otorgados',
            data: [total],
            borderWidth: 1,
            backgroundColor: 'rgba(230, 123, 23, 0.75)',
            borderColor: 'rgb(230, 123, 23)',
            barThickness: 70
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

const montoGraph = document.getElementById('graph-monto');
new Chart(montoGraph, {
    type: 'bar',
    data: {
        labels: ['Monto total otorgado'],
        datasets: [{
            label: 'Monto total otorgado',
            data: [monto],
            borderWidth: 1,
            barThickness: 70
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

const distribuciones = document.getElementById('graph-clientes');
new Chart(distribuciones, {
    type: 'doughnut',
    data: {
        labels: Object.keys(distribucion),
        datasets: [{
            label: 'Monto total otorgado',
            data: Object.values(distribucion),
            borderWidth: 1,
        }]
    },
    options: {
    }
});

const distribucionesCantidad = document.getElementById('graph-clientes-cantidad');
new Chart(distribucionesCantidad, {
    type: 'bar',
    data: {
        labels: Object.keys(cantidad),
        datasets: [{
            label: 'Monto total otorgado',
            data: Object.values(cantidad),
            borderWidth: 1,
            barThickness: 70
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});