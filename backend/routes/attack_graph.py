from fastapi import APIRouter
import requests

router = APIRouter(prefix="/attack")

@router.post("/graph")
def graph(vulns:list):
    r = requests.post(
        "http://localhost:9000/attack-graph",
        json=vulns
    )
    return r.json()
