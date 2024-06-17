import community as community_louvain
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import networkx as nx

import urllib.request
import io
import zipfile

GG_Karate = nx.karate_club_graph ()

gmlFootball = "F:\\SNA LAB\\SNA LAB EXAM\\football.gml"

GG_Football = nx.read_gml (gmlFootball)

gmlDolphin = "F:\\SNA LAB\\SNA LAB EXAM\\dolphins.gml"

GG_Dolphin = nx.read_gml (gmlDolphin)

partitionKarate = community_louvain.best_partition (GG_Karate)
partitionFootball = community_louvain.best_partition (GG_Football)
partitionDolphin = community_louvain.best_partition (GG_Dolphin)

def print_community_info(partition):
    communities = {}
    for node, community in partition.items():
        if community in communities:
            communities[community].append(node)
        else:
            communities[community] = [node]
    num_communities = len(communities)
    print(f"Number of communities: {num_communities}")
    for i, nodes in communities.items():
        num_nodes = len(nodes)
        print(f"Community {i+1}: {num_nodes} nodes")

#print("Karate Club Network:")
#print_community_info(partitionKarate)

#print("\n\nFootBall Club Network")
#print_community_info(partitionFootball)

print("\n\nDolphin Club Network")
print_community_info(partitionDolphin)

# Drawing the Graph
posKarate = nx.spring_layout (GG_Karate)
posFootball = nx.spring_layout (GG_Football)
posDolphin = nx.spring_layout (GG_Dolphin)

plt.figure (figsize = (15, 15))
plt.title ("KARATE CLUB NETWORK")
cmap = cm.get_cmap ('viridis', max (partitionKarate.values ()) + 1)
nx.draw_networkx_nodes (GG_Karate, posKarate, partitionKarate.keys (), node_size = 40, cmap = cmap, node_color = list (partitionKarate.values ()))
nx.draw_networkx_edges (GG_Karate, posKarate, alpha = 0.5)

plt.figure (figsize = (15, 15))
plt.title ("FOOTBALL CLUB NETWORK")
cmap = cm.get_cmap ('viridis', max (partitionFootball.values ()) + 1)
nx.draw_networkx_nodes (GG_Football, posFootball, partitionFootball.keys (), node_size = 40, cmap = cmap, node_color = list (partitionFootball.values ()))
nx.draw_networkx_edges (GG_Football, posFootball, alpha = 0.5)

plt.figure (figsize = (15, 15))
plt.title ("DOLPHIN NETWORK NETWORK")
cmap = cm.get_cmap ('viridis', max (partitionDolphin.values ()) + 1)
nx.draw_networkx_nodes (GG_Dolphin, posDolphin, partitionDolphin.keys (), node_size = 40, cmap = cmap, node_color = list (partitionDolphin.values ()))
nx.draw_networkx_edges (GG_Dolphin, posDolphin, alpha = 0.5)

plt.show ()