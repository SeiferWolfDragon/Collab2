from app import app,db
from app.models.post import Post
from app.models.category import Category

with app.app_context():
    db.create_all()

    def create_data():
        # Verificar si la categoría con ID 2 existe, si no existe, crearla
        category = Category.query.get(2)
        if category is None:
            print("La categoría con ID 2 no existe. Creándola...")
            category = Category(id=2, name="Cryptocurrency")
            db.session.add(category)
            db.session.commit()
        
        # Ahora insertar el post con category_id=2
        post = Post(
            title="Bitcoin alcanza su máximo histórico en 2023",
            content="El Bitcoin ha superado nuevamente las expectativas al alcanzar un nuevo máximo histórico de $45,000 este mes, impulsado por la adopción masiva de criptomonedas...",
            category_id=2
        )
        db.session.add(post)
        db.session.commit()
        print("Post creado exitosamente.")

    # Llamar a la función para insertar los datos
    create_data()