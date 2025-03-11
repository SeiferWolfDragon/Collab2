from app import db

# Definir la tabla `Category`
class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)  # Aumentar longitud a 255 si es necesario
    
    # Relación con la tabla `Post` (uno a muchos)
    posts = db.relationship('Post', backref='category', lazy=True)

    def __repr__(self):
        return f'<Category {self.name}>'