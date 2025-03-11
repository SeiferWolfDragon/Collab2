import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

# Crear instancia
app = Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Importar modelos para que SQLAlchemy los reconozca
from app.models.post import Post
from app.models.category import Category

@app.route('/')
def index():
    return render_template('home.html')

# Importar y registrar los blueprints
from app.routes.post import posts_bp
app.register_blueprint(posts_bp, url_prefix='/posts')