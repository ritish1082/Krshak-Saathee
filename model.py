import pickle
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Load csv file
crop_data = pd.read_csv('Crop Recommendation dataset.csv')

# independent and dependent variables
x = crop_data.drop(columns=['CROP'])
y = crop_data['CROP']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Train Values
model = DecisionTreeClassifier()
model.fit(x_train.values, y_train.values)

# # Convert To Pickle
pickle.dump(model, open('model.pkl', 'wb'))
