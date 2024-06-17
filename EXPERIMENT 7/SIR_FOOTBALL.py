import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import networkx as nx

# Load the network from the GML file
file_path = "C:\\Users\\91839\\Desktop\\SNA LAB\\EXPERIMENT 7\\football.gml"
G = nx.read_gml(file_path)

# Define the SIR model equations
def sir_model(y, t, beta, gamma, N):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Calculate the total number of nodes in the network
N = len(G.nodes)

# Set initial conditions
I0 = 1  # Initial number of infected individuals
S0 = N - I0
R0 = 0

# Set parameters
beta = 0.3  # Contact rate
gamma = 0.1  # Recovery rate

# Time vector
t = np.linspace(0, 160, 160)

# Initial conditions vector
y0 = S0, I0, R0

# Integrate the SIR equations over the time grid, t
ret = odeint(sir_model, y0, t, args=(beta, gamma, N))
S, I, R = ret.T

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(t, S, 'b', alpha=0.7, linewidth=2, label='Susceptible')
plt.plot(t, I, 'r', alpha=0.7, linewidth=2, label='Infected')
plt.plot(t, R, 'g', alpha=0.7, linewidth=2, label='Recovered')
plt.xlabel('Time (days)')
plt.ylabel('Number of individuals')
plt.title('SIR Model on Football Club Network')
plt.legend(loc='best')
plt.grid(1)
plt.show()
