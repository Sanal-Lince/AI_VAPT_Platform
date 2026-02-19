from fastapi import APIRouter
import subprocess

router = APIRouter(prefix="/scan")

@router.get("/port")
def scan(target:str):
    result = subprocess.getoutput(f"nmap -F {target}")
    return {"output":result}
