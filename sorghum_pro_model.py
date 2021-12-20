import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pickle

df = pd.read_csv('harvest production dataset.csv')

sorghum = df[['Dist Code', 'Year', 'SORGHUM AREA (1000 ha)', 'SORGHUM PRODUCTION (1000 Quintal)',
            'SORGHUM HARVEST PRICE (Rs per Quintal)']]
sorghum = sorghum.interpolate(method='linear')

# sorghum regression-model-1

sorghum_X1 = sorghum.drop(columns=['SORGHUM PRODUCTION (1000 Quintal)', 'SORGHUM HARVEST PRICE (Rs per Quintal)'])
sorghum_y1 = sorghum['SORGHUM PRODUCTION (1000 Quintal)']

sorghum_X1_train, sorghum_X1_test, sorghum_y1_train, sorghum_y1_test = train_test_split(sorghum_X1, sorghum_y1, test_size=0.2)

sorghum_model_1 = linear_model.LinearRegression()
sorghum_model_1.fit(sorghum_X1_train, sorghum_y1_train)

# pickle file
pickle.dump(sorghum_model_1, open("sorghum_pro_model.pkl", "wb"))