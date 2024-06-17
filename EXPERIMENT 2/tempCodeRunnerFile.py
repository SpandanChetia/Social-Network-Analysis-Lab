import networkx as nx
import matplotlib.pyplot as plt

def generate_er_graph(n, p):
    # Generate Erdos-Renyi random graph
    er_graph = nx.erdos_renyi_graph(n, p)
    return er_graph

def visualize_graph(graph):
    # Visualize the graph
    nx.draw(graph, with_labels=True, font_weight='bold')
    plt.show()

# Take inputs from the user
n = int(input("Enter the number of nodes (n): "))
p = float(input("Enter the probability of edge creation (p): "))

# Generate and visualize the Erdos-Renyi random graph
er_graph = generate_er_graph(n, p)
visualize_graph(er_graph)
