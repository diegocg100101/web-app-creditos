# Créditos Web App 

Esta aplicación permite gestionar créditos otorgados y mostrar gráficos que representen la información ingresada. 

### Instalación
Para correr el proyecto se requiere seguir los siguientes pasos a continuación

#### 1. Clonar el repositorio
Para clonar el repositorio se debe ejecutar el siguiente comando en una terminal Git:

```
git clone <url_del_repositorio>
```

#### 2. Activar el entorno virtual
Se debe ejecutar el siguiente comando dentro del directorio del proyecto para activar el entorno virtual de Python que contiene las librerías necesarias para funcionar. 

```
. .venv/bin/activate
```

#### 3. Iniciar el servidor
Dentro del archivo app.py se encuentran importadas todas las configuraciones necesarias para que la aplicación pueda funcionar correctamente con SQLite a través del ORM SQLAlchemy, así como las rutas, modelos y vistas. Para correr el proyecto se debe ejecutar la siguiente línea de comando:
```
python3 app.py
``` 

## API endpoints

| Endpoint       | Descripción                                                                 |
| -------------- | --------------------------------------------------------------------------- |
| **GET  /creditos/add** | Devuelve el template HTML con el formulario.                                |
| **POST /creditos/add** | Registra los datos ingresados del crédito en la base de datos.              |  
| **GET /creditos/list** | Devuelve todos los créditos ingresados a la base de datos.                  |
| **DELETE /creditos/delete/{id}** | Elimina en la base de datos el crédito correspondiente al ID.     |    
| **GET /creditos/edit/{id}** | Devuelve el template HTML con el formulario con los datos de la entidad correspondiente al ID. |
| **POST /creditos/edit/{id}** | Actualiza los datos la instancia correspondiente al ID.               | 
| **GET /creditos/graph**  | Devuelve la cantidad total de créditos otorgados, el monto total otorgado, los montos otorgados por cliente y la cantidad de créditos otorgados por cliente.                  |



### Página principal

## CRUD

### Registrar crédito

### Lista de créditos

## Gráficos



