import requests
import sqlite3

API_KEY = 'a550234ea2461f8e0cbd4e4332fa9aaa'
BASE_URL = 'https://api.themoviedb.org/3/movie/popular?api_key=' + API_KEY

def get_movies():
    response = requests.get(BASE_URL)
    return response.json()['results']

def insert_movies(movies):
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()
    for movie in movies:
        c.execute('''
            INSERT INTO movies (id, title, overview, vote_average)
            VALUES (?, ?, ?, ?)
        ''', (movie['id'], movie['title'], movie['overview'], movie['vote_average']))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    movies = get_movies()
    insert_movies(movies)
