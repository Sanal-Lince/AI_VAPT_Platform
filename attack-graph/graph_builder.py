import networkx as nx

def build_attack_graph(vulns):
 G=nx.DiGraph()
 for v in vulns:
  G.add_edge(v["source"],v["target"])
 return G
