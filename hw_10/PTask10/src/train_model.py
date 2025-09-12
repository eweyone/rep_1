import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv('../data/realty_datasss.csv')
df = df[['price', 'total_square', 'floor']].dropna()

X = df[['total_square', 'floor']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

with open('../models/model.pkl', 'wb') as file:
    pickle.dump(model, file)