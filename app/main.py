from fastapi import FastAPI
from app.features import hash_feature

app = FastAPI()


@app.get("/predict")
def predict(text: str):
    """
    Simple prediction endpoint.
    """
    bucket = hash_feature(text)
    return {"bucket": bucket}
