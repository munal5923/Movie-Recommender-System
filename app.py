import streamlit as st
from src.recommend import get_movie_list, recommend

st.header("Movie Recommender System")

movie_list = get_movie_list()
selected_movie = st.selectbox("Type or select a movie:", movie_list)

if st.button("Show Recommendation"):
    recommendations = recommend(selected_movie)
    for rec in recommendations:
        st.text(rec["title"])
        st.image(rec["poster_url"])