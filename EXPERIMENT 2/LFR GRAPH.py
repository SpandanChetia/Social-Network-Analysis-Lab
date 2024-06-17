import networkx as nx
from networkx.generators.community import LFR_benchmark_graph
import matplotlib.pyplot as plt

# Parameters for LFR graph
num_nodes = 100
tau1 = 3.0  # Power-law exponent for the degree distribution of the created graph
tau2 = (
    1.5  # Power-law exponent for the community size distribution in the created graph
)
mu = 0.1  # Fraction of intra-community edges to total edges
average_degree = 10  # Average degree of nodes in the created graph

# Generate LFR graph
lfr_graph = LFR_benchmark_graph(num_nodes, tau1, tau2, mu, average_degree, seed=42)

# Draw the graph
pos = nx.spring_layout(lfr_graph)
nx.draw(
    lfr_graph, pos, with_labels=True, node_size=50, node_color="skyblue", font_size=8
)
plt.title("LFR Benchmark Graph")
plt.show()