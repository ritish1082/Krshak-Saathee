import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pickle

df = pd.read_csv('harvest production dataset.csv')

sorghum = df[['Dist Code','Year','SORGHUM AREA (1000 ha)','SORGHUM PRODUCTION (1000 Quintal)','SORGHUM HARVEST PRICE (Rs per Quintal)']]
sorghum = sorghum.interpolate(method='linear')

#sorghum regression-model-2

sorghum_X2 = sorghum.drop(columns=['Dist Code','SORGHUM HARVEST PRICE (Rs per Quintal)'])
sorghum_y2 = sorghum['SORGHUM HARVEST PRICE (Rs per Quintal)']

sorghum_X2_train, sorghum_X2_test, sorghum_y2_train, sorghum_y2_test = train_test_split(sorghum_X2, sorghum_y2, test_size = 0.2)

sorghum_model_2 = linear_model.LinearRegression()
sorghum_model_2.fit(sorghum_X2, sorghum_y2)

#pickle file
pickle.dump(sorghum_model_2, open('sorghum_pri_model.pkl', 'wb'))