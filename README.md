# Movie-Recommender-System-Using-Machine-Learning

This project is a movie recommender system that allows users to select a movie and get recommendations based on a dataset of movies and their similarities. The system fetches movie posters from The Movie Database (TMDb) API to display with the recommended movies.

## Features
- **Movie Selection**: Users can type or select a movie from a dropdown list.
- **Recommendations**: Once a movie is selected, the app recommends 5 similar movies.
- **Movie Posters**: Movie posters are fetched from TMDb and displayed alongside movie names.

## Setup

To run this application locally, follow these steps:

### Prerequisites
1. Python 3.x installed.
2. Install the required libraries using pip:
   ```bash
   pip install streamlit pandas requests
   ```

3. Run the Movie Recommender System Data Analysis.ipynb to get the necessary pickle files:
   - `movie_list.pkl` - Contains a list of movies.
   - `similarity.pkl` - Contains the precomputed similarity matrix used for recommendations.

4. Get an API key from [TMDb](https://www.themoviedb.org/) to fetch movie posters.

### Running the Application
1. Place the `app.py` script and the required `artifacts` folder (containing `movie_list.pkl` and `similarity.pkl`) in the same directory.
2. Run the Streamlit app using the following command:
   ```bash
   streamlit run app.py
   ```
3. Visit the local URL provided (usually `http://localhost:8501/`) in your web browser to start using the app.

## How It Works

1. **Movie Selection**: When the user selects a movie from the dropdown, the app uses the movie's title to find its index in the movie list.
2. **Similarity Calculation**: The app calculates the similarity between the selected movie and others using a precomputed similarity matrix. The movies with the highest similarity are recommended.
3. **Poster Fetching**: For each recommended movie, the app fetches a poster using the movie's ID from The Movie Database API.
4. **Display Recommendations**: The app displays the movie names along with their posters in a grid layout.

## Files
- **`app.py`**: The main application file that runs the Streamlit web app.
- **`movie_list.pkl`**: Pickle file containing the list of movies used for recommendations.
- **`similarity.pkl`**: Pickle file containing the precomputed similarity matrix used to suggest similar movies.
