from sqlalchemy.orm import Session
from backend.models import Movie
from backend.database import SessionLocal

def get_all_movies():
    db = SessionLocal()
    movies = db.query(Movie).all()
    db.close()
    return movies
