from fastapi import FastAPI
from backend import crud
from .database import get_movie_by_id, get_all_movies

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de recommandations de films 🎬"}

@app.get("/movies/")
def read_movies():
    return crud.get_all_movies()