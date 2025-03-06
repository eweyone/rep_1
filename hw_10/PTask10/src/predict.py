import pickle
import numpy as np

with open('models/model.pkl', 'rb') as file:
    model = pickle.load(file)

def predict_price(total_square: float, floor: int):
    features = np.array([[total_square, floor]])
    return model.predict(features)[0]