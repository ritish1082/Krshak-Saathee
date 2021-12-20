import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pickle

df = pd.read_csv('harvest production dataset.csv')

gnut = df[['Dist Code','Year','GROUNDNUT AREA (1000 ha)','GROUNDNUT PRODUCTION (1000 Quintal)','GROUNDNUT HARVEST PRICE (Rs per Quintal)']]
gnut = gnut.interpolate(method='linear')

#gnut regression-model-2

gnut_X2 = gnut.drop(columns=['Dist Code','GROUNDNUT HARVEST PRICE (Rs per Quintal)'])
gnut_y2 = gnut['GROUNDNUT HARVEST PRICE (Rs per Quintal)']

gnut_X2_train, gnut_X2_test, gnut_y2_train, gnut_y2_test = train_test_split(gnut_X2, gnut_y2, test_size = 0.2)

gnut_model_2 = linear_model.LinearRegression()
gnut_model_2.fit(gnut_X2, gnut_y2)

#pickle file
pickle.dump(gnut_model_2, open('groundnut_pri_model.pkl', 'wb'))