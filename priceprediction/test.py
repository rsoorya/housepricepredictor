import json
import pickle
import numpy as np


global __model
global __data_columns
global __locations

with open('model/columns.json','r') as f:
    __data_columns = json.load(f)['data_columns']
    __locations = __data_columns[3:]

with open('model/bangalore_home_prices_model.pickle','rb') as f:
    __model = pickle.load(f)

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1]=bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)

#print(get_estimated_price("1st Phase JP Nagar",1000,3,3))
#print(get_estimated_price("Indira Nagar",1000,3,3))

