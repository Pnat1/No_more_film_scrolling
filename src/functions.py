
import pandas as pd

def cleanstryear(x):
    '''
    This function clean my column year database from string characters
    '''
    if x == 'TV Movie 2019':
        return 2019
    else:
        return x


def movie_recommend(original_title):
    '''
    Fuction computes top 10 recommendation given a movie title
    '''
    idx = indices[original_title]
    sim_scores = list(enumerate(cosine_similarities[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:31]
    movie_indices = [i[0] for i in sim_scores]

    return movie_title.iloc[movie_indices]
