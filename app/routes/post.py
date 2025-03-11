from flask import Blueprint, request, jsonify, render_template, url_for, redirect
from app import db
from app.models.post import Post
from app.models.category import Category

posts_bp = Blueprint('posts', __name__)

# Ruta para ver todos los posts
@posts_bp.route('/')
def listar_posts():
    posts = Post.query.all()
    categories = Category.query.all()
    return render_template('posts/listar_posts.html', posts=posts, categories=categories)

# Ruta /post crear un nuevo post
@posts_bp.route('/post/new', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category_id = request.form.get('category_id')
        new_post = Post(title=title, content=content, category_id=category_id)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('posts.listar_posts'))
    
    # Aqui sigue si es GET
    categories = Category.query.all()
    return render_template('posts/create_post.html', categories=categories)

# Actualizar post
@posts_bp.route('/post/update/<int:id>', methods=['GET', 'POST'])
def update_post(id):
    post = Post.query.get(id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.category_id = request.form['category_id']
        post.content = request.form['content']
        db.session.commit()
        return redirect(url_for('posts.listar_posts'))
    
    categories = Category.query.all()
    return render_template('update_post.html', post=post, categories=categories)

# Eliminar post
@posts_bp.route('/posts/delete/<int:id>')
def delete_post(id):
    post = Post.query.get(id)
    if post:
        db.session.delete(post)
        db.session.commit()
    return redirect(url_for('posts.listar_posts'))
