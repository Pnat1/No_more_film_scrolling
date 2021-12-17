from re import T
import streamlit as st
from PIL import Image
import pandas as pd
import seaborn as sns
import matplotlib as plt
import plotly.express as px 
import plotly.graph_objects as go
import plotly.figure_factory as ff
import src.data_sys as das



def app():
 
    st.title("\U0001f3ac Movie Dataset Graphs \U0001f3ac")
    #Imagenes de Kaggle y otras tech utilizadas para data processing

    st.write("""
        ## Lets dive into the data with visuals \U0001f3ca
        """)
    
    size1 = ["Genre", "Country", "Duration", "Year", "Language", "Random Country"]
    input_size = st.selectbox("Choose", size1)


    if input_size == "Genre":

        st.write("""
        ### Top 10 Movie Genres Produced
        """)
        img1 = Image.open('images/pie_10.png')
        st.image(img1)

    elif input_size == "Country":

        st.write("""
        ### Film Production by Country
        """)
        img2 = Image.open('images/country.jpg')
        st.image(img2)

    elif input_size == "Duration":

        st.write("""
        ### Distribution of Film Time Duration
        """)
        img3 = Image.open('images/distribution_duration.jpg')
        st.image(img3)

    elif input_size == "Year":

        st.write("""
        ### Movie Productioon per year History
        """)
        img4 = Image.open('images/mov_prod_year.jpg')
        st.image(img4)

    elif input_size == "Language":
        st.write("""
        ### Language Use
        """)
        img5 = Image.open('images/language.PNG')
        st.image(img5)

    else:

        st.write("""
        ### Top 10 Genres Produced in East Germany
        """)
        img6 = Image.open('images/drop_pie.jpg')
        st.image(img6)

    

