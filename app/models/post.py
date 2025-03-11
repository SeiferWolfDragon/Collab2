from app import db

# Definir la tabla `Post`
class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)  # Aumentar longitud a 255
    content = db.Column(db.Text, nullable=False)  # No se necesita cambiar esto, ya que `Text` permite texto largo
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='SET NULL'), nullable=True)
    
    def __repr__(self):
        return f'<Post {self.title}>'