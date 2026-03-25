from fastapi import FastAPI
from pydantic import BaseModel
from engine import estimate_cost

app = FastAPI()

class Request(BaseModel):
    product: str
    price: float
    category: str
    brand: str
    channel: str

@app.get("/")
def root():
    return {"message": "TrueCost API running"}

@app.post("/estimate")
def estimate(req: Request):
    return estimate_cost(
        req.product,
        req.price,
        req.category,
        req.brand,
        req.channel
    )
