from re import T
import streamlit as st
from PIL import Image
import pandas as pd
#import  src.get_movies as gmov
#import src.get_movies_plus as gplus 
import src.data_sys as das
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


data = das.chargedatasys()
    # Tengo que crear una nueva solumna con los parámetros que aparecen abajo de duración

def vetorize_text_cosine(stuff):
    tfid = TfidfVectorizer()
    features = tfid.fit_transform(stuff)
    cosine_sim_mat = cosine_similarity(features)
    return cosine_sim_mat


def get_recommendation(title, cosine_sim_mat, num_of_rec=5):

    index = pd.Series(data.index,index=data['original_title']).drop_duplicates()
    idx = index[index == title].index[0]
    score = list(enumerate(cosine_sim_mat[idx]))
    score = sorted(score,key=lambda x: x[1], reverse=True)
    selected_course_idx = [i[0] for i in score[1:]]
    selected_course_scores = [i[0] for i in score[1:]]


    result_data = data.iloc[selected_course_idx]
    return result_data
    #for i in top10:
    #    movies.append(data[i])
    #return movies


def app():

    st.title("\U0001f3ac Movie Recommender System! \U0001f3ac")
        #Imagenes de Kaggle y otras tech utilizadas para data processing
    st.subheader('Python Content & User Recommender System ')

    cosine_sim_mat = vetorize_text_cosine(data['original_title'])
    genre_search = st.text_input("Choose Genre")
    num_of_rec = st.selectbox.number_input("Number", 5, 10)
    if st.button("Recommend"):
        if genre_search is not None:
            try:
                result = get_recommendation(genre_search, cosine_sim_mat, data, num_of_rec)
            except:
                result = "Not Found"
                st.write(result)



    










  #  input_duration = ["0 < 1h","1h < 1h30m","1h30m < 2h", "2h < 2h30m", "2h30m < 3h", "3h+"]
  #  duration = st.selectbox("Select film duration", input_duration)
  #  if duration == input_duration:
   #     st.stop()




    page_bg_img = '''
    <style>
        .stApp {
    background-image: url("https://payload.cargocollective.com/1/11/367710/13568488/MOVIECLASSICSerikweb_2500_800.jpg");
    background-size: cover;
    }
    </style>
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)
