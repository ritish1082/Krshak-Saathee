import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pickle

df = pd.read_csv('harvest production dataset.csv')

sesamum = df[['Dist Code','Year','SESAMUM AREA (1000 ha)','SESAMUM PRODUCTION (1000 Quintal)','SESAMUM HARVEST PRICE (Rs per Quintal)']]
sesamum = sesamum.interpolate(method='linear')

#sesamum regression-model-2

sesamum_X2 = sesamum.drop(columns=['Dist Code','SESAMUM HARVEST PRICE (Rs per Quintal)'])
sesamum_y2 = sesamum['SESAMUM HARVEST PRICE (Rs per Quintal)']

sesamum_X2_train, sesamum_X2_test, sesamum_y2_train, sesamum_y2_test = train_test_split(sesamum_X2, sesamum_y2, test_size = 0.2)

sesamum_model_2 = linear_model.LinearRegression()
sesamum_model_2.fit(sesamum_X2, sesamum_y2)

#pickle file
pickle.dump(sesamum_model_2, open('sesamum_pri_model.pkl', 'wb'))