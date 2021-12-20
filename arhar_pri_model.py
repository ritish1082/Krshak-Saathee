import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pickle

df = pd.read_csv('harvest production dataset.csv')

arhar = df[['Dist Code','Year','ARHAR AREA (1000 ha)','ARHAR PRODUCTION (1000 Quintal)','ARHAR HARVEST PRICE (Rs per Quintal)']]
arhar = arhar.interpolate(method='linear')

#arhar regression-model-2

arhar_X2 = arhar.drop(columns=['Dist Code','ARHAR HARVEST PRICE (Rs per Quintal)'])
arhar_y2 = arhar['ARHAR HARVEST PRICE (Rs per Quintal)']

arhar_X2_train, arhar_X2_test, arhar_y2_train, arhar_y2_test = train_test_split(arhar_X2, arhar_y2, test_size = 0.2)

arhar_model_2 = linear_model.LinearRegression()
arhar_model_2.fit(arhar_X2, arhar_y2)

#pickle file
pickle.dump(arhar_model_2, open('arhar_pri_model.pkl', 'wb'))