import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pickle

df = pd.read_csv('harvest production dataset.csv')

paddy = df[['Dist Code', 'Year', 'PADDY AREA (1000 ha)', 'PADDY PRODUCTION (1000 Quintal)',
            'PADDY HARVEST PRICE (Rs per Quintal)']]
paddy = paddy.interpolate(method='linear')

# paddy regression-model-1

paddy_X1 = paddy.drop(columns=['PADDY PRODUCTION (1000 Quintal)', 'PADDY HARVEST PRICE (Rs per Quintal)'])
paddy_y1 = paddy['PADDY PRODUCTION (1000 Quintal)']

paddy_X1_train, paddy_X1_test, paddy_y1_train, paddy_y1_test = train_test_split(paddy_X1, paddy_y1, test_size=0.2)

paddy_model_1 = linear_model.LinearRegression()
paddy_model_1.fit(paddy_X1_train, paddy_y1_train)

# pickle file
pickle.dump(paddy_model_1, open("paddy_pro_model.pkl", "wb"))