from fastapi import FastAPI
from graph_builder import build_attack_graph

app=FastAPI()

@app.post("/attack-graph")
def graph(vulns:list):
 g=build_attack_graph(vulns)
 return {"nodes":list(g.nodes),"edges":list(g.edges)}
