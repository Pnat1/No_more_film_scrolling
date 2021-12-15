from re import T
import streamlit as st
from PIL import Image
import pandas as pd


def app():


    header = st.container()
    dataset1 = st.container()
    dataset2 = st.container()


    with header:
        st.title("\U0001f3ac Movie Datasets! \U0001f3ac")
        #Imagenes de Kaggle y otras tech utilizadas para data processing
        st.subheader('IMDd movie and movie-rating datasets found on www.kaggle.com')

    with dataset1:
        # Transición cronológica de tu data set
        st.header('IMDb Movie Description Datasets')
        st.caption('')

        movies1 = pd.read_csv('data/imdb_movies.csv')
        st.write(movies1.head())


        st.caption('Data Processing and Transformation')
        movies2 = pd.read_csv('data/imdb_movies_clean_1st.csv')
        st.write(movies2.head())


    with dataset2:
        #Transición cronológica de ratigs dattaset
        st.header('IMDb Movie Rating Datasets')
        st.caption('')

        ratings = pd.read_csv('data/IMDb_ratings.csv')
        st.write(ratings.head())