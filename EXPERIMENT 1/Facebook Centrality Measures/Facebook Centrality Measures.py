import networkx as nx
import matplotlib.pyplot as plt
import csv

csv_file_path = "C:\\Users\\91839\\Desktop\\SNA LAB\\EXPERIMENT 1\\Facebook Centrality Measures\\fb_csv.csv"

# Read the graph from the CSV file
with open(csv_file_path, 'r') as file:
    # Assuming the CSV file has two columns representing edges
    # For example: node1, node2
    csv_reader = csv.reader(file)
    edges = [(row[0], row[1]) for row in csv_reader]

# Create a graph from the list of edges
G = nx.Graph(edges)

# Centrality
deg_cen = nx.degree_centrality(G)
bet_cen = nx.betweenness_centrality(G)
eigen_cen = nx.eigenvector_centrality(G)

print(deg_cen)
print(bet_cen)
print(eigen_cen)



# Visualization
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="purple", node_size=200, font_size=5)
plt.title("Network with Centrality")
plt.show()
