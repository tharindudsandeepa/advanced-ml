from pathlib import Path
from typing import Literal

import joblib
import pandas as pd

from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field

BASE_DIR=Path(__file__).resolve().parent
MODEL_PATH=BASE_DIR/"mlr_mpg_v1.joblib"

app =FastAPI(title="MLR MPG Prediction API",
             description="An API to predict miles per gallon (MPG)",
             version="1.0.0"
)

class PredictionReqeuest(BaseModel):
    displacement: float = Field(..., description="Engine Displacement in cubic inches")
    horsepower:float = Field(...,description="Engine horsepower"),
    weight:float = Field(...,description="Weight of the car in pounds"),
    acceleration:float = Field(...,description="Time to accelerate from 0 to 60 mph in seconds"),
    model_year:int = Field(...,description="Model year of the car"),
    origin:int = Field(...,description="Origin of the Car."),
    cylinders:int = Field(...,description="Cylinders of the Car.")

class PredictionResponse(BaseModel):
    predicted_mpg: float = Field(...,description="Predicted miles per gallon (MPG) for the Car")


def load_model(model_path: Path):
    if not model_path.exists():
        raise FileNotFoundError(f"Model file not found at {model_path}")
    return joblib.load(model_path)

try:
    model=load_model(MODEL_PATH)
except FileNotFoundError as e:
    raise RuntimeError(f"Failed to load model: {e}")
else:
    model_load_err=None

def build_inference_frame(request: PredictionReqeuest) -> pd.DataFrame:
    return pd.DataFrame([{
        "displacement": request.displacement,
        "horsepower": request.horsepower,
        "weight": request.weight,
        "acceleration": request.acceleration,
        "model year": request.model_year,
        "origin": request.origin,
        "cylinders": request.cylinders
    }])

@app.post("/predict",response_model=PredictionResponse)
def predict(request: PredictionReqeuest):
    if model_load_err is not None:
        raise HTTPException(status_code=500,detail=f"Model failed to load: {model_load_err}")

    inference_frame =build_inference_frame(request)
    predicted_mpg = model.predict(inference_frame)[0]
    return PredictionResponse(predicted_mpg=predicted_mpg)

