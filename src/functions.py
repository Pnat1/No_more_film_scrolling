
import pandas as pd

def cleanstryear(x):
    '''
    This function clean my column year database from string characters
    '''
    if x == 'TV Movie 2019':
        return 2019
    else:
        return x


