import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pickle

df = pd.read_csv('harvest production dataset.csv')

sesamum = df[['Dist Code', 'Year', 'SESAMUM AREA (1000 ha)', 'SESAMUM PRODUCTION (1000 Quintal)',
            'SESAMUM HARVEST PRICE (Rs per Quintal)']]
sesamum = sesamum.interpolate(method='linear')

# sesamum regression-model-1

sesamum_X1 = sesamum.drop(columns=['SESAMUM PRODUCTION (1000 Quintal)', 'SESAMUM HARVEST PRICE (Rs per Quintal)'])
sesamum_y1 = sesamum['SESAMUM PRODUCTION (1000 Quintal)']

sesamum_X1_train, sesamum_X1_test, sesamum_y1_train, sesamum_y1_test = train_test_split(sesamum_X1, sesamum_y1, test_size=0.2)

sesamum_model_1 = linear_model.LinearRegression()
sesamum_model_1.fit(sesamum_X1_train, sesamum_y1_train)

# pickle file
pickle.dump(sesamum_model_1, open("sesamum_pro_model.pkl", "wb"))