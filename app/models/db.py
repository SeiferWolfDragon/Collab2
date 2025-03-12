# app/models/db.py
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Inicializar SQLAlchemy
db = SQLAlchemy()
