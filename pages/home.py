from re import T
from numpy import True_
import streamlit as st
from PIL import Image
import pandas as pd
import streamlit.components.v1 as stc




def app():

    st.title("\U0001f3ac No More Film Scrolling! \U0001f3ac")
    img = Image.open('images/movie_posters.jpg')
    
    
    st.image(img, use_column_width=True_)


    st.write("""
    ## Motivation behind the project
    
    ### *No More Film Scrolling, * find the correct movie in a couple of seconds

    #### This movie recommender system is built to widen your film taste horizons while it takes into accout your demmands
    
    """)
    img = Image.open('images/family_movies.jpg')
    st.image(img)
    


