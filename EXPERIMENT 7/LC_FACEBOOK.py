import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import networkx as nx
import csv  # Import the csv module

csv_file_path = r"C:/Users/91839/Desktop/SNA LAB/EXPERIMENT 7/fb_csv.csv"  # Use raw string or forward slashes

# Read the graph from the CSV file
with open(csv_file_path, 'r') as file:
    # Assuming the CSV file has two columns representing edges
    # For example: node1, node2
    csv_reader = csv.reader(file)
    edges = [(row[0], row[1]) for row in csv_reader]

# Create a graph from the list of edges
G = nx.Graph(edges)

# Define the Linear Cascades model equations
def linear_cascades_model(y, t, beta, N):
    I = y
    adjacency_matrix = nx.to_numpy_array(G)
    dIdt = beta * np.dot(adjacency_matrix, I) - beta * I
    return dIdt

# Calculate the total number of nodes in the network
N = len(G.nodes)

# Set initial conditions
I0 = np.zeros(N)
I0[0] = 1  # Initial activation at node 0

# Set parameters
beta = 0.1  # Cascade rate

# Time vector
t = np.linspace(0, 160, 160)

# Integrate the Linear Cascades equations over the time grid, t
ret = odeint(linear_cascades_model, I0, t, args=(beta, N))
I = ret.T

# Plot the data
plt.figure(figsize=(10, 6))
for i in range(N):
    plt.plot(t, I[i], alpha=0.7)

plt.xlabel('Time (days)')
plt.ylabel('Activation level')
plt.title('Linear Cascades Model on FACEBOOK Network')
plt.legend(loc='best')
plt.grid(1)
plt.show()
