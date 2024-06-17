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