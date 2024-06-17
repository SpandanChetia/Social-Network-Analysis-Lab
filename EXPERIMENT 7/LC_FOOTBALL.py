import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import networkx as nx

# Load the network from the GML file
file_path = "C:\\Users\\91839\\Desktop\\SNA LAB\\EXPERIMENT 7\\football.gml"
G = nx.read_gml(file_path)

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
plt.title('Linear Cascades Model on Football Club Network')
plt.legend(loc='best')
plt.grid(1)
plt.show()
