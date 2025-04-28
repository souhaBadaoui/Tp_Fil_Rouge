import requests
from database import SessionLocal, Film

# Clé API TMDB (remplace par ta clé)
API_KEY = "a550234ea2461f8e0cbd4e4332fa9aaa"
MOVIE_ID = 550  # Fight Club

# Requête API
url = f"https://api.themoviedb.org/3/movie/{MOVIE_ID}?api_key={API_KEY}"
response = requests.get(url)
data = response.json()

# Transformation des genres en texte
genres = ", ".join([genre["name"] for genre in data.get("genres", [])])

# Sauvegarde dans SQLite
db = SessionLocal()
film = Film(
    id=data["id"],
    title=data["title"],
    overview=data["overview"],
    genres=genres,
    vote_average=data["vote_average"],
    vote_count=data["vote_count"],
    release_date=data["release_date"]
)

db.add(film)
db.commit()
db.close()

print(f"✅ Film '{data['title']}' ajouté à la base SQLite !")
