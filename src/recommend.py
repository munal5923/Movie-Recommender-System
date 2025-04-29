import pickle
import pandas as pd
from src.tmdb import fetch_poster

# Load data once
with open("artifacts/movie_list.pkl", "rb") as f:
    movies = pickle.load(f)

with open("artifacts/similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

def get_movie_list():
    return movies['title'].values

def recommend(movie_title):
    index = movies[movies['title'] == movie_title].index[0]
    distances = sorted(enumerate(similarity[index]), key=lambda x: x[1], reverse=True)[1:6]
    
    results = []
    for i in distances:
        movie_id = movies.iloc[i[0]].movie_id
        results.append({
            "title": movies.iloc[i[0]].title,
            "poster_url": fetch_poster(movie_id)
        })
    
    return results
