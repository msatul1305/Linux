import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes
G.add_node(1)
G.add_nodes_from([2, 3])

# Add edges
G.add_edge(1, 2)
G.add_edges_from([(1, 3), (2, 3)])

# Draw the graph
nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, edge_color='black', linewidths=1, font_size=15)

# Display the graph
plt.show()
