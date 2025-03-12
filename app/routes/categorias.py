from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models.category import Category

categories_bp = Blueprint('categories', __name__)

# Listar todas las categorías
@categories_bp.route('/')
def listar_categorias():
    categories = Category.query.all()
    return render_template('categorias/listarCategorias.html', categories=categories)

# Crear nueva categoría
@categories_bp.route('/category/new', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        name = request.form['name']
        new_category = Category(name=name)
        db.session.add(new_category)
        db.session.commit()
        return redirect(url_for('categories.listar_categorias'))

    return render_template('categorias/create_category.html')

# Actualizar categoría
@categories_bp.route('/category/update/<int:id>', methods=['GET', 'POST'])
def update_category(id):
    category = Category.query.get(id)
    if request.method == 'POST':
        category.name = request.form['name']
        db.session.commit()
        return redirect(url_for('categories.listar_categorias'))

    return render_template('categorias/update_category.html', category=category)

# Eliminar categoría
@categories_bp.route('/category/delete/<int:id>')
def delete_category(id):
    category = Category.query.get(id)
    if category:
        db.session.delete(category)
        db.session.commit()
    return redirect(url_for('categories.listar_categorias'))
