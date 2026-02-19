import subprocess

services = [
 ["python","ai-engine/predict.py"],
 ["python","attack-graph/graph_api.py"],
 ["python","llm-report/report_api.py"],
 ["python","backend/main.py"]
]

for s in services:
    subprocess.Popen(s)

print("All services started")
