import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

def train_model():
    try:
        df = pd.read_csv('../data/datapt.csv')

        df = df[['price', 'total_square', 'floor']].dropna()

        x = df[['total_square', 'floor']]
        y = df['price']

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

        model = LinearRegression()
        model.fit(x_train, y_train)

        if not os.path.exists('models'):
            os.makedirs('models')

        with open('models/model.pkl', 'wb') as f:
            pickle.dump(model, f)

        print("Модель обучена и сохранена в 'models/model.pkl'")

    except Exception as e:
        print(f"Ошибка: {e}")

train_model()