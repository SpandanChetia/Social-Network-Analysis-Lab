import matplotlib.pyplot as plt 
import networkx as nx 

gml_file_path = "C:\\Users\\91839\\Desktop\\EXPERIMENT 1\\Dolphin Centrality Measures\\dolphins.gml"

# Read the graph from the GraphML file
G = nx.read_gml(gml_file_path)

# Calculate degree centrality
degree_centrality = nx.degree_centrality(G)

# Print degree centrality for each node
print("\nDEGREE CENTRALITY")
for node, centrality in degree_centrality.items():
     print(f"Node {node}: = {centrality}")

# Calculate betweenness centrality
betweenness_centrality = nx.betweenness_centrality(G)

# Print betweenness centrality for each node
print("\nBETWEENESS CENTRALITY")
for node, centrality in betweenness_centrality.items():
    print(f"Node {node}: = {centrality}")

# Calculate eigenvector centrality
eigenvector_centrality = nx.eigenvector_centrality(G)

# Print eigenvector centrality for each node
print("\nEIGEN VECTOR CENTRALITY")
for node, centrality in eigenvector_centrality.items():
    print(f"Node {node}: = {centrality}")

# Visualize the network
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='purple', node_size=800, font_size=8)
plt.title("Dolphin Club Network with Degree Centrality")
plt.show()
