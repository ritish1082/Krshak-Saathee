import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pickle

df = pd.read_csv('harvest production dataset.csv')

gnut = df[['Dist Code', 'Year', 'GROUNDNUT AREA (1000 ha)', 'GROUNDNUT PRODUCTION (1000 Quintal)',
            'GROUNDNUT HARVEST PRICE (Rs per Quintal)']]
gnut = gnut.interpolate(method='linear')

# gnut regression-model-1

gnut_X1 = gnut.drop(columns=['GROUNDNUT PRODUCTION (1000 Quintal)', 'GROUNDNUT HARVEST PRICE (Rs per Quintal)'])
gnut_y1 = gnut['GROUNDNUT PRODUCTION (1000 Quintal)']

gnut_X1_train, gnut_X1_test, gnut_y1_train, gnut_y1_test = train_test_split(gnut_X1, gnut_y1, test_size=0.2)

gnut_model_1 = linear_model.LinearRegression()
gnut_model_1.fit(gnut_X1_train, gnut_y1_train)

# pickle file
pickle.dump(gnut_model_1, open("groundnut_pro_model.pkl", "wb"))