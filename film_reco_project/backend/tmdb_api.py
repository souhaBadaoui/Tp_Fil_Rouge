import requests

API_KEY = "a550234ea2461f8e0cbd4e4332fa9aaa"
BASE_URL = "https://api.themoviedb.org/3"

def get_movie_details(movie_id):
    """Récupère les détails d'un film via l'API TMDB"""
    url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "id": data["id"],
            "title": data["title"],
            "overview": data["overview"],
            "genres": [genre["name"] for genre in data["genres"]],
            "vote_average": data["vote_average"],
            "release_date": data["release_date"]
        }
    else:
        print(f"Erreur {response.status_code} : Impossible de récupérer le film.")
        return None

# Tester avec un film (Fight Club ID: 550)
if __name__ == "__main__":
    movie = get_movie_details(550)
    print(movie)