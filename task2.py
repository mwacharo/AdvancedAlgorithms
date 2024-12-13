import heapq
import random

# Dijkstra's algorithm
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        for neighbor, weight in graph.get(current_node, []):
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Allocate the closest driver
def allocate_driver(graph, takeaway_location):
    distances = dijkstra(graph, takeaway_location)
    drivers = {node: distances[node] for node in distances if "Driver" in node}

    if not drivers:
        return drivers, "No drivers available!"

    closest_driver = min(drivers, key=drivers.get)
    return drivers, closest_driver


def get_custom_graph():
    print("\nCustom Graph Input Mode\n")
    graph = {}

    while True:
        try:
            nodes_input = input("Enter the number of nodes (locations like Takeaway, Driver1, Customer1, etc.) or type '0' for an empty graph: ").strip()
            if nodes_input == '0':  # Allow explicitly creating an empty graph
                print("You have chosen to create an empty graph.")
                return graph
            nodes = int(nodes_input)
            if nodes < 1:
                print("Number of nodes must be at least 1 or 0 for an empty graph. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer or '0' for an empty graph.")

    for node_index in range(1, nodes + 1):
        while True:
            node = input(f"Enter node name for node {node_index}/{nodes} (e.g., Takeaway, Driver1, Customer1): ").strip()
            if not node:
                print("Node name cannot be empty. Please enter a valid name.")
                continue
            if node in graph:
                print("This node already exists. Please enter a unique name.")
                continue
            break

        edges = int(input(f"How many edges (connections) does {node} have? "))
        neighbors = []

        for _ in range(edges):
            while True:
                neighbor = input(f"Enter neighbor for {node}: ").strip()
                if not neighbor:
                    print("Neighbor name cannot be empty. Please enter a valid name.")
                    continue
                try:
                    distance = int(input(f"Enter distance from {node} to {neighbor}: "))
                    if distance <= 0:
                        print("Distance must be greater than 0. Try again.")
                        continue
                    neighbors.append((neighbor, distance))
                    break
                except ValueError:
                    print("Invalid input. Distance must be a positive integer.")

        graph[node] = neighbors

    # Validate graph scenarios dynamically
    if "Takeaway" not in graph:
        print("Graph must include a 'Takeaway' node. Restarting...")
        return get_custom_graph()

    drivers = [node for node in graph if "Driver" in node]
    if not drivers:
        print("Warning: No drivers found in the graph. Deliveries may not be possible.")

    customers = [node for node in graph if "Customer" in node]
    if not customers:
        print("Warning: No customers found in the graph. Please ensure customers exist.")

    return graph
def generate_large_graph(num_nodes=100):
    graph = {}

    # Create nodes
    nodes = [f"Node{i}" for i in range(1, num_nodes + 1)]

    # Assign special roles
    takeaway = "Takeaway"
    drivers = [f"Driver{i}" for i in range(1, 6)]  # 5 Drivers
    customers = [f"Customer{i}" for i in range(1, 6)]  # 5 Customers
    nodes = [takeaway] + drivers + customers + nodes[len(drivers) + len(customers) + 1:]

    for node in nodes:
        # Random number of edges (between 1 and 5 for simplicity)
        num_edges = random.randint(1, 5)
        neighbors = []

        for _ in range(num_edges):
            neighbor = random.choice(nodes)
            if neighbor != node:  # Avoid self-loops
                distance = random.randint(1, 20)  # Random distance between 1 and 20
                neighbors.append((neighbor, distance))

        graph[node] = neighbors

    return graph


# Main function
def main():
    print("Welcome to the Fast Food Delivery System")
    choice = input("Would you like to use default graph data or enter your own? (Enter 'default' or 'custom'or 'random'): ").strip().lower()

    # Default graph data
    default_graph = {
        "Takeaway": [("Driver1", 3), ("Driver2", 5), ("Customer1", 2)],
        "Driver1": [("Takeaway", 3), ("Customer2", 4)],
        "Driver2": [("Takeaway", 5), ("Customer1", 7)],
        "Customer1": [("Takeaway", 2), ("Driver2", 7)],
        "Customer2": [("Driver1", 4)]
    }

    if choice == 'default':
        graph = default_graph
    elif choice == 'custom':
        graph = get_custom_graph()
    elif choice =='random':
        graph = generate_large_graph(100)   
    else:
        print("Invalid choice. Using default graph data.")
        graph = default_graph

    # Prompt for the Takeaway location and find the closest driver
    takeaway_location = "Takeaway"
    drivers, closest_driver = allocate_driver(graph, takeaway_location)

    # Display all drivers and their distances
    print("\nDrivers near the Takeaway and their distances:")
    if drivers:
        for driver, distance in drivers.items():
            print(f"{driver}: {distance} units away")
    else:
        print("No drivers available!")

    # Display the closest driver
    if closest_driver != "No drivers available!":
        print(f"\nThe closest driver to the {takeaway_location} is {closest_driver}")
    else:
        print(closest_driver)

if __name__ == "__main__":
    main()
