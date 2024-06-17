import networkx as nx
import matplotlib.pyplot as plt
import random

# Load the network from the GML file
file_path = "C:\\Users\\91839\\Desktop\\SNA LAB\\EXPERIMENT 7\\dolphins.gml"
G = nx.read_gml(file_path)

# Model Parameters
infection_probability = 0.1  # Probability of infection per contact
max_time_steps = 50

# Check for a valid initial infected node index
if G.number_of_nodes() > 0:
    initial_infected_node = random.choice(list(G.nodes))
    G.nodes[initial_infected_node]['status'] = 'I'  # 'I' for infected
else:
    raise ValueError("The network does not contain any nodes.")

# Set 'status' attribute to 'S' for all nodes
nx.set_node_attributes(G, 'S', 'status')

# Linear Cascade Epidemic Model Simulation
susceptible_count = []
infected_count = []

def linear_cascade_model(graph, initial_infected, infection_prob, max_time_steps):
    for _ in range(max_time_steps):
        # Count the number of individuals in each compartment
        susceptible_count.append(sum(1 for node in graph.nodes() if graph.nodes[node]['status'] == 'S'))
        infected_count.append(sum(1 for node in graph.nodes() if graph.nodes[node]['status'] == 'I'))

        # Linear Cascade Infection
        for edge in graph.edges():
            source, target = edge
            if graph.nodes[source]['status'] == 'I' and graph.nodes[target]['status'] == 'S':
                if random.random() < infection_prob:
                    graph.nodes[target]['status'] = 'I'  # Infect the target node

# Run the Linear Cascade model
linear_cascade_model(G, initial_infected_node, infection_probability, max_time_steps)

# Plot the epidemic model graph
plt.subplot(1, 2, 1)
node_colors = {'S': 'blue', 'I': 'red'}
node_colors = [node_colors[G.nodes[node]['status']] for node in G.nodes]
pos = nx.spring_layout(G)  # Positioning nodes for better visualization
nx.draw(G, pos, with_labels=True, node_color=node_colors)
plt.title("Linear Cascade Model on Dolphin Club Dataset")

# Plot the number of individuals vs days
plt.subplot(1, 2, 2)
days = list(range(1, max_time_steps + 1))
plt.plot(days, susceptible_count, label='Susceptible', color='blue')
plt.plot(days, infected_count, label='Infected', color='red')
plt.xlabel('Days')
plt.ylabel('Number of Individuals')
plt.title('Linear Cascade Model: Number of Individuals vs Days')
plt.legend()
plt.grid(1)

plt.tight_layout()  # Adjust layout for better spacing
plt.show()
