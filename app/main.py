# importing required dependencies
from fastapi import FastAPI

# initiating fastapi app
app = FastAPI(
    title="House Price Prediction API",
    description="An API for predicting house prices",
    version="1.0.0",
)

# endpoints
@app.get("/")
def read_root():
    return {"message": "this is the root of house price prediction API"}

@app.get("/health")
def read_health():
    return {"status": "ok"}
