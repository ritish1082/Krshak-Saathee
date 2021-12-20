import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pickle

df = pd.read_csv('harvest production dataset.csv')

arhar = df[['Dist Code', 'Year', 'ARHAR AREA (1000 ha)', 'ARHAR PRODUCTION (1000 Quintal)',
            'ARHAR HARVEST PRICE (Rs per Quintal)']]
arhar = arhar.interpolate(method='linear')

# arhar regression-model-1

arhar_X1 = arhar.drop(columns=['ARHAR PRODUCTION (1000 Quintal)', 'ARHAR HARVEST PRICE (Rs per Quintal)'])
arhar_y1 = arhar['ARHAR PRODUCTION (1000 Quintal)']

arhar_X1_train, arhar_X1_test, arhar_y1_train, arhar_y1_test = train_test_split(arhar_X1, arhar_y1, test_size=0.2)

arhar_model_1 = linear_model.LinearRegression()
arhar_model_1.fit(arhar_X1_train, arhar_y1_train)

# pickle file
pickle.dump(arhar_model_1, open("arhar_pro_model.pkl", "wb"))