from fastapi import FastAPI
from routes import scan, ai, report, attack_graph

app = FastAPI(title="AI VAPT CORE")

app.include_router(scan.router)
app.include_router(ai.router)
app.include_router(report.router)
app.include_router(attack_graph.router)
