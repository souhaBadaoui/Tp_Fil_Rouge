# backend/seed.py

from backend.database import Base, engine, SessionLocal
from backend.models import Movie

# Crée les tables (si ce n'est pas déjà fait)
Base.metadata.create_all(bind=engine)

# Connexion à la base
db = SessionLocal()

# Liste des films à insérer
movies = [
    Movie(id=1, title="Inception", genres="Action, Sci-Fi", vote_average=8.8),
    Movie(id=2, title="Interstellar", genres="Adventure, Drama, Sci-Fi", vote_average=8.6),
    Movie(id=3, title="The Dark Knight", genres="Action, Crime, Drama", vote_average=9.0),
    Movie(id=4, title="Fight Club", genres="Drama", vote_average=8.8),
]

# Insertion si la base est vide
if db.query(Movie).count() == 0:
    db.add_all(movies)
    db.commit()
    print("✅ Base de données peuplée avec succès !")
else:
    print("⚠️ La base de données contient déjà des films.")

db.close()
