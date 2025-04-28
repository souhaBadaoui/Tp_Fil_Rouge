from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Fonction pour recommander des films en fonction de la description
def recommend_movies_based_on_description(df, movie_id):
    # Utilisation de TF-IDF pour transformer les descriptions des films
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['overview'])

    # Calcul de la similarité cosinus entre tous les films
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Trouver l'index du film que l'utilisateur a sélectionné
    idx = df[df['id'] == movie_id].index[0]

    # Calcul des similarités avec tous les autres films
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # On exclut le film lui-même et on garde les 5 films les plus similaires
    sim_scores = sim_scores[1:6]
    recommended_movie_ids = [df.iloc[i[0]]['id'] for i in sim_scores]

    return recommended_movie_ids

