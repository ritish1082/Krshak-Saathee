import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pickle

df = pd.read_csv('harvest production dataset.csv')

paddy = df[['Dist Code','Year','PADDY AREA (1000 ha)','PADDY PRODUCTION (1000 Quintal)','PADDY HARVEST PRICE (Rs per Quintal)']]
paddy = paddy.interpolate(method='linear')

#paddy regression-model-2

paddy_X2 = paddy.drop(columns=['Dist Code','PADDY HARVEST PRICE (Rs per Quintal)'])
paddy_y2 = paddy['PADDY HARVEST PRICE (Rs per Quintal)']

paddy_X2_train, paddy_X2_test, paddy_y2_train, paddy_y2_test = train_test_split(paddy_X2, paddy_y2, test_size = 0.2)

paddy_model_2 = linear_model.LinearRegression()
paddy_model_2.fit(paddy_X2, paddy_y2)

#pickle file
pickle.dump(paddy_model_2, open('paddy_pri_model.pkl', 'wb'))