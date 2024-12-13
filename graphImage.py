# import networkx as nx
# import matplotlib.pyplot as plt

# # Define the graph as an adjacency list
# graph = {
#     "Takeaway": [("Driver1", 3), ("Driver2", 5), ("Customer1", 2)],
#     "Driver1": [("Customer2", 4)],
#     "Driver2": [("Customer1", 7)],
#     "Customer1": [],
#     "Customer2": []
# }

# # Create a directed graph
# G = nx.DiGraph()

# # Add edges to the graph with weights
# for node, neighbors in graph.items():
#     for neighbor, weight in neighbors:
#         G.add_edge(node, neighbor, weight=weight)

# # Position nodes using spring layout
# pos = nx.spring_layout(G)

# # Draw the graph
# plt.figure(figsize=(8, 6))
# nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold', arrowsize=20)
# labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red', font_size=8)

# # Save the graph as an image
# plt.title("Graph Representation of Locations")
# plt.savefig("graph_screenshot.png")  # Save the graph as a PNG file
# plt.show()