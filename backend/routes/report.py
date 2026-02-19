from fastapi import APIRouter
import requests

router = APIRouter(prefix="/report")

@router.post("/generate")
def generate(vulns:list):
    r = requests.post(
        "http://localhost:9100/generate-report",
        json=vulns
    )
    return r.json()
