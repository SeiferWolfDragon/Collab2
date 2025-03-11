from app import app, db
from flask import render_template, request, redirect, url_for
from app.models import Category, Post

# Asegúrate de que la tabla exista
with app.app_context():
    db.create_all()

    # Agregar categorías predefinidas si no existen
    predefined_categories = ['Política', 'Economía', 'Deportes', 'Cultura y entretenimiento']
    for category_name in predefined_categories:
        if not Category.query.filter_by(name=category_name).first():
            new_category = Category(name=category_name)
            db.session.add(new_category)
    db.session.commit()

# Asegúrate de que el directorio de plantillas esté configurado correctamente
app.template_folder = 'templates'

@app.route('/create_post')
def create_post():
    categories = Category.query.all()
    return render_template('posts/create_post.html', categories=categories)

@app.route('/submit_post', methods=['POST'])
def submit_post():
    title = request.form['title']
    content = request.form['content']
    category_id = request.form['category_id']
    new_post = Post(title=title, content=content, category_id=category_id)
    db.session.add(new_post)
    db.session.commit()
    return redirect(url_for('create_post'))

# Ruta para listar categorías
@app.route('/categories')
def list_categories():
    categories = Category.query.all()
    return render_template('categories/list_categories.html', categories=categories)

# Ruta para crear una nueva categoría
@app.route('/categories/new', methods=['GET', 'POST'])
def new_category():
    if request.method == 'POST':
        name = request.form['name']
        new_category = Category(name=name)
        db.session.add(new_category)
        db.session.commit()
        return redirect(url_for('list_categories'))
    return render_template('categories/new_category.html')

# Ruta para editar una categoría
@app.route('/categories/edit/<int:id>', methods=['GET', 'POST'])
def edit_category(id):
    category = Category.query.get_or_404(id)
    if request.method == 'POST':
        category.name = request.form['name']
        db.session.commit()
        return redirect(url_for('list_categories'))
    return render_template('categories/edit_category.html', category=category)

# Ruta para eliminar una categoría
@app.route('/categories/delete/<int:id>', methods=['POST'])
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('list_categories'))

if __name__ == "__main__":
    app.run(debug=True)