from re import T
import streamlit as st
from PIL import Image
import pandas as pd 



def app():


    header = st.container()
    dataset1 = st.container()
    images = st.container()
    dataset2 = st.container()


    with header:
        st.title("\U0001f3ac Movie Datasets! \U0001f3ac")
        #Imagenes de Kaggle y otras tech utilizadas para data processing
        st.subheader('IMDd movie web-scrapped dataset with more than 85,000 films found on www.kaggle.com')

    with dataset1:
        # Transición cronológica de tu data set
        st.header('IMDb Movie Description Dataset')
        st.subheader('Initial dataset')

        movies1 = pd.read_csv('data/imdb_movies.csv')
        st.write(movies1.head())

    with images:
        img = Image.open('images/processing.jpg')
        st.image(img)   


    with dataset2:
        #Transición cronológica de ratigs dattaset
        st.header('End Product')
        st.subheader('After Data Cleaning and Processing')

        ratings = pd.read_csv('data/clean_title_input_movies.csv')
        st.write(ratings.head())