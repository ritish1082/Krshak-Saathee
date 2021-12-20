from sklearn import linear_model
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle

df = pd.read_csv('district_data.csv')
district_X=df[['Year']]
district_y=df[['ARHAR PRODUCTION (1000 Quintal)']]
district_X1_train, district_X1_test, district_y1_train, district_y1_test = train_test_split(district_X, district_y, test_size = 0.2)
district = linear_model.LinearRegression()
district.fit(district_X1_train, district_y1_train)

#pickle file
pickle.dump(district, open('arhar_district_model.pkl', 'wb'))