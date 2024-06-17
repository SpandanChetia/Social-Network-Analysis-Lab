import networkx as nx
import matplotlib.pyplot as plt
import random

# Load the network from the GML file
file_path = "C:\\Users\\91839\\Desktop\\SNA LAB\\EXPERIMENT 7\\dolphins.gml"
G = nx.read_gml(file_path)

# Model Parameters
initial_infected_node = random.choice(list(G.nodes))
infection_probability = 0.1  # Probability of infection per contact
recovery_probability = 0.05  # Probability of recovery per time step
max_time_steps = 50

# Set 'status' attribute to 'S' for all nodes
nx.set_node_attributes(G, 'S', 'status')
G.nodes[initial_infected_node]['status'] = 'I'  # 'I' for infected

# SIR Epidemic Model Simulation
susceptible_count = []
infected_count = []
recovered_count = []

def sir_epidemic_model(graph, initial_infected, infection_prob, recovery_prob, max_time_steps):
    for _ in range(max_time_steps):
        # Count the number of individuals in each compartment
        susceptible_count.append(sum(1 for node in graph.nodes() if graph.nodes[node]['status'] == 'S'))
        infected_count.append(sum(1 for node in graph.nodes() if graph.nodes[node]['status'] == 'I'))
        recovered_count.append(sum(1 for node in graph.nodes() if graph.nodes[node]['status'] == 'R'))

        for node in graph.nodes():
            if graph.nodes[node]['status'] == 'I':  # If the node is infected
                neighbors = list(graph.neighbors(node))
                for neighbor in neighbors:
                    if graph.nodes[neighbor]['status'] == 'S':  # If the neighbor is susceptible
                        if random.random() < infection_prob:
                            graph.nodes[neighbor]['status'] = 'I'  # Infect the neighbor

        # Recovery phase
        for node in graph.nodes():
            if graph.nodes[node]['status'] == 'I' and random.random() < recovery_prob:
                graph.nodes[node]['status'] = 'R'  # Recover the node

# Run the SIR model
sir_epidemic_model(G, initial_infected_node, infection_probability, recovery_probability, max_time_steps)

# Plot the epidemic model graph

node_colors = {'S': 'blue', 'I': 'red', 'R': 'green'}
node_colors = [node_colors[G.nodes[node]['status']] for node in G.nodes]
pos = nx.spring_layout(G)  # Positioning nodes for better visualization
nx.draw(G, pos, with_labels=True, node_color=node_colors)
plt.title("SIR Epidemic Model on Dolphin Club Dataset")
plt.show()
# Plot the number of individuals vs days

days = list(range(1, max_time_steps + 1))
plt.plot(days, susceptible_count, label='Susceptible', color='blue')
plt.plot(days, infected_count, label='Infected', color='red')
plt.plot(days, recovered_count, label='Recovered', color='green')
plt.xlabel('Days')
plt.ylabel('Number of Individuals')
plt.title('SIR Epidemic Model: Number of Individuals vs Days')
plt.legend()
plt.grid(1)

plt.tight_layout()  # Adjust layout for better spacing
plt.show()
