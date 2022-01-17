
# Introduction

This is my final project for the Data Analysis course done at Ironhack Bootcamp Madrid. 

I have decided to create a film recomender system using content and collaborative procedures depending on the individualidarity of the user genre tastes and time constraints. The project aims to sum up many of the tools and knowledge learned throughout the two month intensive bootcamp.


# Project Objectives

- Obtain a substantially big movie dataset with movie descriptions, ratings, votes. The chosen site was IMDb as it also had an accesible API to do request from. Yet, in the end I found appropiate alrady web-scrapped datatsets in Kaggle.

- Proper understanding of data through data Cleaning/Processing and Visualizations. 

- Tidy organisation of the project where ultimately each file must be dedicated to one process in particular.

- Use more than one machine learning model to recommend films to users

- Develop a user vosualization tool, Streamlit will be used for this.

- Upload the streamlit page to internet.


# Repository & Project Structure

- config: Folder containing a file wit the projects basic configuration connections.
- data : Folder containing all the raw and cleaned datasets used.
- images : Images used for through presentation and project.
- notebooks : 
    * cleaning : Cleaning of data Notebook.
    * recommending : Recommending machine learning models.
    * visualization : Visual graphs representing the data with storytelling.
- src:
    * data_sys.py : Contains data gathering functions connecting the Jupyter noteoobook and the streamlit VSC page.
    * get_visual.py : Contains visualitation graph functions calling to the jupyter notebook and connecting with the Streamlit page.
- main.py : Contains all the main call for the streamlit page.
- multipage.py : Multi APP use definition page.

# Movie Recomending System

