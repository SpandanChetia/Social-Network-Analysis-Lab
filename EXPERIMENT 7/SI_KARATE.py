import networkx as nx
import matplotlib.pyplot as plt
import random

# Load Karate Club dataset
G = nx.karate_club_graph()

# Model Parameters
initial_infected_node = 0  # Initial infected node
infection_probability = 0.1  # Probability of infection per contact
max_time_steps = 50

# Initialize node attributes
nx.set_node_attributes(G, 'S', 'status')  # 'S' for susceptible
G.nodes[initial_infected_node]['status'] = 'I'  # 'I' for infected

# SI Epidemic Model Simulation
susceptible_count = []
infected_count = []

def si_epidemic_model(graph, initial_infected, infection_prob, max_time_steps):
    for _ in range(max_time_steps):
        # Count the number of individuals in each compartment
        susceptible_count.append(sum(1 for node in graph.nodes() if graph.nodes[node]['status'] == 'S'))
        infected_count.append(sum(1 for node in graph.nodes() if graph.nodes[node]['status'] == 'I'))

        for node in graph.nodes():
            if graph.nodes[node]['status'] == 'I':  # If the node is infected
                neighbors = list(graph.neighbors(node))
                for neighbor in neighbors:
                    if graph.nodes[neighbor]['status'] == 'S':  # If the neighbor is susceptible
                        if random.random() < infection_prob:
                            graph.nodes[neighbor]['status'] = 'I'  # Infect the neighbor

# Run the SI model
si_epidemic_model(G, initial_infected_node, infection_probability, max_time_steps)

# Plot the epidemic model graph
plt.subplot(1, 2, 1)
node_colors = {'S': 'blue', 'I': 'red'}
node_colors = [node_colors[G.nodes[node]['status']] for node in G.nodes]
pos = nx.spring_layout(G)  # Positioning nodes for better visualization
nx.draw(G, pos, with_labels=True, node_color=node_colors)
plt.title("SI Epidemic Model on Karate Club Dataset")

# Plot the number of individuals vs days
plt.subplot(1, 2, 2)
days = list(range(1, max_time_steps + 1))
plt.plot(days, susceptible_count, label='Susceptible', color='blue')
plt.plot(days, infected_count, label='Infected', color='red')
plt.xlabel('Days')
plt.ylabel('Number of Individuals')
plt.title('SI Epidemic Model: Number of Individuals vs Days')
plt.legend()
plt.grid(1)

plt.tight_layout()  # Adjust layout for better spacing
plt.show()
