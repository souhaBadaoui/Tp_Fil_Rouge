from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connexion à SQLite
DATABASE_URL = "sqlite:///./films.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

from sqlalchemy.orm import Session
from .models import Movie

def get_all_movies(db: Session):
    return db.query(Movie).all()

def get_movie_by_id(db: Session, movie_id: int):
    return db.query(Movie).filter(Movie.id == movie_id).first()