from fastapi import APIRouter
from ai_engine.predict import predict_risk

router = APIRouter(prefix="/ai")

@router.post("/analyze")
def analyze(data:list):
    return {"risk":predict_risk(data)}
