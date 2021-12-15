from re import T
import streamlit as st
from PIL import Image
import pandas as pd
from multipage import MultiPage
from pages import home
from pages import datasets
from pages import graphs
from pages import recommender



app = MultiPage()


app.add_page("Home", home.app)
app.add_page("Data", datasets.app)
app.add_page("Graphs", graphs.app)
app.add_page("Recommender", recommender.app)


app.run()


