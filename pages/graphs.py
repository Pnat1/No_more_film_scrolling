from re import T
import streamlit as st
from PIL import Image
import pandas as pd


def app():

    header = st.container()

    with header:
        st.title("\U0001f3ac Movie Dataset Graphs \U0001f3ac")
        #Imagenes de Kaggle y otras tech utilizadas para data processing
        st.subheader('IMDd movie and movie-rating graphs')

