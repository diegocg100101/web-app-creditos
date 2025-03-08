from app import create_app

if __name__ == '__main__':
    """
    Llama a la función para ejecutar la confguración de la base de datos y Blueprints 
    antes de correr la aplicación.
    """
    app = create_app()
    app.run(debug=True)