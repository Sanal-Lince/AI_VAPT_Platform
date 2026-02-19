from fastapi import FastAPI
from report_generator import generate_report

app=FastAPI()

@app.post("/generate-report")
def report(vulns:list):
 return {"report":generate_report(vulns)}
