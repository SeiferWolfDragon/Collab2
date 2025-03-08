from flask import Flask

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Definir una ruta para la página principal
@app.route('/')
def hello_world():
    return '¡Hola, Mundo!'

# Comentario para rama dev

if __name__ == '__main__':
    app.run(debug=True)
