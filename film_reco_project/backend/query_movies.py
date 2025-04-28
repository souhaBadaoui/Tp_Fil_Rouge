from database import SessionLocal, Film

db = SessionLocal()
films = db.query(Film).all()
db.close()

for film in films:
    print(f"{film.id}: {film.title} - {film.vote_average}/10")
