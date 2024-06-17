import networkx as nx
import matplotlib.pyplot as plt

def generate_barabasi_albert_graph(n, m):
    # Generate Barabasi-Albert random graph
    barabasi_albert_graph = nx.barabasi_albert_graph(n, m)
    return barabasi_albert_graph

def visualize_graph(graph):
    # Visualize the graph
    nx.draw(graph, with_labels=True, font_weight='bold')
    plt.show()

# Take inputs from the user
n = int(input("Enter the number of nodes (n): "))
m = int(input("Enter the number of edges per new node (m): "))

# Generate and visualize the Barabasi-Albert random graph
ba_graph = generate_barabasi_albert_graph(n, m)
visualize_graph(ba_graph)
