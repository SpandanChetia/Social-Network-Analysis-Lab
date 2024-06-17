import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import networkx as nx
import csv

csv_file_path = r"C:/Users/91839/Desktop/SNA LAB/EXPERIMENT 7/fb_csv.csv"

# Read the graph from the CSV file
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    edges = [(row[0], row[1]) for row in csv_reader]

# Create a graph from the list of edges
G = nx.Graph(edges)

# Define the SI model equations
def si_model(y, t, beta, N):
    S, I = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N
    return dSdt, dIdt

# Calculate the total number of nodes in the network
N = len(G.nodes)

# Set initial conditions
I0 = 1  # Initial number of infected individuals
S0 = N - I0

# Set parameter
beta = 0.3  # Contact rate

# Time vector
t = np.linspace(0, 160, 160)

# Initial conditions vector
y0 = S0, I0

# Integrate the SI equations over the time grid, t
ret = odeint(si_model, y0, t, args=(beta, N))
S, I = ret.T

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(t, S, 'b', alpha=0.7, linewidth=2, label='Susceptible')
plt.plot(t, I, 'r', alpha=0.7, linewidth=2, label='Infected')
plt.xlabel('Time (days)')
plt.ylabel('Number of individuals')
plt.title('SI Model on FACEBOOK Network')
plt.legend(loc='best')
plt.grid(1)
plt.show()
