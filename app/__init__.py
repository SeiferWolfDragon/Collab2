from flask import Flask
#comentario de prueba
#comentario para verificar que funciona el push en mi propia rama
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola Mundo'

if __name__ == '__main__':
    app.run(debug=True)