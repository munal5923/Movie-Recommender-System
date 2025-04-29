import requests

def fetch_poster(movie_id: int) -> str:
    api_key = "your_tmdb_api_key_here"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    response = requests.get(url).json()
    return "https://image.tmdb.org/t/p/w500/" + response['poster_path']