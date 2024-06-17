import random
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity


def generate_random_ground_truth(G, positive_ratio=0.1, negative_ratio=0.1):
    existing_edges = list(G.edges())
    num_positive_samples = int(len(existing_edges) * positive_ratio)
    num_negative_samples = int((len(G.nodes()) * (len(G.nodes()) - 1) / 2 - len(existing_edges)) * negative_ratio)

    positive_samples = random.sample(existing_edges, num_positive_samples)

    all_possible_pairs = [(i, j) for i in range(len(G.nodes())) for j in range(i + 1, len(G.nodes())) if not G.has_edge(i, j)]
    negative_samples = random.sample(all_possible_pairs, num_negative_samples)

    ground_truth = positive_samples + negative_samples
    random.shuffle(ground_truth)

    return ground_truth


# Generate or load your graph
G = nx.karate_club_graph()

# Calculate adjacency matrix
adj_matrix = nx.adjacency_matrix(G)

# Calculate cosine similarity matrix
cos_sim_matrix = cosine_similarity(adj_matrix)

# Threshold to predict links for Cosine Similarity
threshold_cosine = 0.5  # Adjust as needed
predicted_links_cosine = [(i, j) for i in range(len(G.nodes())) for j in range(i + 1, len(G.nodes())) if
                          cos_sim_matrix[i][j] > threshold_cosine]

print("Number of predicted links using Cosine Similarity:", len(predicted_links_cosine))


# Calculate Jaccard coefficient for all pairs of nodes
jaccard_coefficient = list(nx.jaccard_coefficient(G))

# Threshold to predict links for Jaccard Index
threshold_jaccard = 0.1  # Adjust as needed
predicted_links_jaccard = [(u, v) for (u, v, p) in jaccard_coefficient if p > threshold_jaccard]

print("Number of predicted links using Jaccard Index:", len(predicted_links_jaccard))


# Ground truth dataset (example)
ground_truth = generate_random_ground_truth(G)

# Calculate True Positives (TP), False Positives (FP), True Negatives (TN), False Negatives (FN)
TP_cosine = len([link for link in predicted_links_cosine if link in ground_truth])
FP_cosine = len(predicted_links_cosine) - TP_cosine
FN_cosine = len(ground_truth) - TP_cosine

TP_jaccard = len([link for link in predicted_links_jaccard if link in ground_truth])
FP_jaccard = len(predicted_links_jaccard) - TP_jaccard
FN_jaccard = len(ground_truth) - TP_jaccard

# Calculate precision
precision_cosine = TP_cosine / (TP_cosine + FP_cosine) if TP_cosine + FP_cosine != 0 else 0
precision_jaccard = TP_jaccard / (TP_jaccard + FP_jaccard) if TP_jaccard + FP_jaccard != 0 else 0

print("Precision using Cosine Similarity:", precision_cosine)
print("Precision using Jaccard Index:", precision_jaccard)