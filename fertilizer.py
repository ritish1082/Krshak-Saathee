import pickle
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import math

# Load csv file
fertilizer_data = pd.read_csv('Fertilizer Prediction.csv')

# independent and dependent variables
x = fertilizer_data.drop(columns=['Fertilizer Name', 'Soil Type'])
y = fertilizer_data['Fertilizer Name']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Scaling Data
# sc = StandardScaler()
# x_train = sc.fit_transform(x_train)
# x_test = sc.transform(x_test)

# Train Values
fertilizer = DecisionTreeClassifier()
fertilizer.fit(x_train, y_train)

# Convert To Pickle
pickle.dump(fertilizer, open('fertilizer.pkl', 'wb'))
