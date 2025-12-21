import networkx as nx
n = 20
L=list(range(n))
G=nx.complete_graph(len(L))
print(n, len(G.edges()))
for e in G.edges():
  print(e[0],e[1])