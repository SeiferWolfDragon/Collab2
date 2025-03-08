import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv 

#Cargar las variables de entorno
load_dotenv()

#crear instancia
app =  Flask(_name_)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#importar modelos para SQLAlchemy los reconozca
from app.models import Post

#importar y registrar los blueprints
from app.routes.post import posts_bp
app.register_blueprint(posts_bp, url_prefix='/posts')

@app.route('/')
def index()
return "Hello World"