from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message":
        "Traffic Prediction API"
    }

@app.get("/predict")
def predict(
    hour: int = 16,
    weekend: int = 0
):
    if weekend == 1:
        prediction = 2600
    else:
        prediction = 3500

    return {
        "Hour": hour,
        "predicted_traffic": prediction
    }