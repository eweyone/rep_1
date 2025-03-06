import pickle
import pandas as pd

def load_model():
    with open('src/models/model.pkl', 'rb') as f:
        return pickle.load(f)

def predict_price(total_square, floor):
    model = load_model()
    data = pd.DataFrame({
        'total_square': [total_square],
        'floor': [floor]
    })
    return model.predict(data)[0]