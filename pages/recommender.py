from re import T
import streamlit as st
from PIL import Image
import pandas as pd


def app():

    header = st.container()

    with header:
        st.title("\U0001f3ac Movie Recommender System! \U0001f3ac")
        #Imagenes de Kaggle y otras tech utilizadas para data processing
        st.subheader('Python Content & User Recommender System ')


    # esto es una función data = dat.cargadata()
    # Tengo que crear una nueva solumna con los parámetros que aparecen abajo de duración

    input_duration = ["0 < 1h","1h < 1h30m","1h30m < 2h", "2h < 2h30m", "2h30m < 3h", "3h+"]
    duration = st.selectbox("Select film duration", input_duration)
    if duration == input_duration:
        st.stop()


    input_genre = ["Otra lista de Géneros principales, se le da más importancia al primero..."]
    genre = st.selectbox("Select film genre", input_genre)
    if genre == input_genre:
        st.stop()

    # formulas

    if duration == "0 < 1h":
        film_time = "0 < 1h" # Alomejor un nombre especíco de mi duturo df
    elif duration == "1h < 1h30m":
        film_time = "1h < 1h30m"
    elif duration == "1h30m < 2h":
        film_time = "1h30m < 2h"
    elif duration == "2h < 2h30m":
        film_time = "2h < 2h30m"
    elif duration == "2h30m < 3h":
        film_time = "2h30m < 3h"
    else:
        film_time = "3h+"
    #watching_time = data[data.duartion.isin(film_time)]