from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import predict_price

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/predict_get")
def predict_get(total_square: float, floor: int):
    price = predict_price(total_square, floor)
    return {"predicted_price": round(price, 2)}

class PredictionInput(BaseModel):
    total_square: float
    floor: int


@app.post("/predict_post")
def predict_post(payload: PredictionInput):

    total_square = payload.total_square
    floor = payload.floor
    price = predict_price(total_square, floor)
    return {"predicted_price": round(price, 2)}