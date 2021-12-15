from re import T
import streamlit as st
from PIL import Image
import pandas as pd



def app():


    header = st.container()
    dataset = st.container()
    features = st.container()
    recommenderSystem = st.container()

    with header:
        st.title("\U0001f3ac No More Film Scrolling! \U0001f3ac")
        img = Image.open('images/movie_posters.jpg')
        st.image(img)
        
        st.subheader('The project develops a Python Recommender Systems to save time in the search of your movie tonight')

    with dataset:
        st.header('IMDb Movie Dataset')
        st.caption('IMDd movie and movie-rating datasets found on www.kaggle.com')

        movies = pd.read_csv('data/imdb_movies_clean_1st.csv')
        st.write(movies.head())


    with features:
        st.header('dont know if i need this ')
        st.text('Probably a list of things done')


    with recommenderSystem:
        st.header('Movie Recommending System!')
        st.text('Model explanation ')