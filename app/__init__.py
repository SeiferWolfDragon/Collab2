# app/__init__.py
import os
from flask import Flask, render_template
from dotenv import load_dotenv
from app.models.db import db  # Importar db desde app.models.db

# Cargar las variables de entorno desde un archivo .env
load_dotenv()

# Crear la instancia de la aplicación Flask
app = Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db.init_app(app)

# Importar los modelos para que SQLAlchemy los reconozca
from app.models import Post, Category  # Aquí se importan los modelos

# Importar y registrar los blueprints
from app.routes.post import posts_bp
from app.routes.categorias import  categories_bp
app.register_blueprint(posts_bp, url_prefix='/posts')
app.register_blueprint(categories_bp, url_prefix='/categorias')

# Definir una ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

