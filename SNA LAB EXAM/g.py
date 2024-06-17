import networkx as nx
import matplotlib.pyplot as plt

def grivan_newman(G):
    G_copy = G.copy()
    betweenness = nx.edge_betweenness_centrality(G_copy)
    edges = sorted(betweenness, key=betweenness.get, reverse=True)
    for edge in edges:
        G_copy.remove_edge(*edge)
        if not nx.is_connected(G_copy):
            break
    return nx.connected_components(G_copy)

football_data = "F:\\SNA LAB\\EXPERIMENT 4\\dolphins.gml"

G = nx.read_gml(football_data)

communities = grivan_newman(G)

pos = nx.spring_layout(G)
plt.figure(figsize=(10, 8))

nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray', linewidths=1, font_size=10)


for i, community in enumerate(communities):
    nx.draw_networkx_nodes(G, pos, nodelist=list(community), node_color=plt.cm.Set1(i), node_size=500)

plt.title("Graph with Communities")
plt.show()
