import random

import networkx as nx
from networkx.algorithms import community
from sklearn.metrics.cluster import normalized_mutual_info_score
import matplotlib.pyplot as plt


def calculate_ANUI(G, communities):
    total_ANUI = 0
    for comm in communities:
        internal_edges = G.subgraph(comm).number_of_edges()
        external_edges = sum(len(set(comm) & set(neigh)) for node in comm for neigh in G.neighbors(node)) / 2
        ANUI = internal_edges / (internal_edges + external_edges)
        total_ANUI += ANUI
    return total_ANUI / len(communities)


def calculate_modularity(G, communities):
    return community.modularity(G, communities)


def calculate_NMI(true_communities, detected_communities):
    true_labels = [i for i, comm in enumerate(true_communities) for _ in comm]
    detected_labels = [i for i, comm in enumerate(detected_communities) for _ in comm]
    return normalized_mutual_info_score(true_labels, detected_labels)


def draw_graph(graph, ax, title):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=False, node_color="yellow", node_size=30, ax=ax)
    ax.set_title(title)


# Load datasets
karate = nx.read_gml("karate.gml")
football = nx.read_gml("football.gml")
dolphin = nx.read_gml("dolphins.gml")

# Detect communities
karate_communities = list(community.louvain_communities(karate))
football_communities = list(community.louvain_communities(football))
dolphin_communities = list(community.louvain_communities(dolphin))

# Calculate metrics
karate_ANUI = calculate_ANUI(karate, karate_communities)
karate_modularity = calculate_modularity(karate, karate_communities)
karate_true_communities = [[node for node in karate.nodes if karate.nodes[node]['club'] == 'Mr. Hi'], [node for node in karate.nodes if karate.nodes[node]['club'] == 'Officer']]
karate_NMI = calculate_NMI(karate_true_communities, karate_communities)

football_ANUI = calculate_ANUI(football, football_communities)
football_modularity = calculate_modularity(football, football_communities)

total_communities = len(football_communities)
football_true = [random.randint(0, total_communities-1) for i in range(len(football))]
football_true_communities = [[] for i in range(total_communities)]
for i in range(len(football)):
    football_true_communities[football_true[i]].append(list(football.nodes)[i])

football_NMI = calculate_NMI(football_true_communities, football_communities)

dolphin_ANUI = calculate_ANUI(dolphin, dolphin_communities)
dolphin_modularity = calculate_modularity(dolphin, dolphin_communities)

total_communities = len(dolphin_communities)
dolphin_true = [random.randint(0, total_communities-1) for i in range(len(dolphin))]
dolphin_true_communities = [[] for i in range(total_communities)]
for i in range(len(dolphin)):
    dolphin_true_communities[dolphin_true[i]].append(list(dolphin.nodes)[i])

dolphin_NMI = calculate_NMI(dolphin_true_communities, dolphin_communities)

# Print results
print("Karate:")
print("ANUI:", karate_ANUI)
print("Modularity:", karate_modularity)
print("NMI:", karate_NMI)

print("\nFootball:")
print("ANUI:", football_ANUI)
print("Modularity:", football_modularity)
print("NMI:", football_NMI)

print("\nDolphin:")
print("ANUI:", dolphin_ANUI)
print("Modularity:", dolphin_modularity)
print("NMI:", dolphin_NMI)

fig, axs = plt.subplots(1, 3, figsize=(12, 12))

draw_graph(karate, axs[0], 'Karate')
draw_graph(football, axs[1], 'Football')
draw_graph(dolphin, axs[2], 'Dolphin')

plt.tight_layout()
plt.show()

