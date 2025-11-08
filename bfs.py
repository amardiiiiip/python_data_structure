from collections import deque

# Function to perform BFS traversal
def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start])  # Initialize queue with starting node
    visited.add(start)  # Mark start as visited
    
    print("BFS Traversal Order:", end=" ")
    while queue:
        node = queue.popleft()  # Dequeue the front node
        print(node, end=" ")  # Visit the node
        
        # Enqueue all unvisited neighbors
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    print()  # New line after traversal


# Main function to take user input and run BFS
def main():
    print("Enter the graph as an adjacency list.")
    print("Format: Number of nodes, then for each node: 'node: neighbor1 neighbor2 ...'")
    print("Example:")
    print("  A: B C")
    print("  B: D")
    print("  C: D")
    print("  D:")
    
    try:
        num_nodes = int(input("\nEnter number of nodes: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    graph = {}
    print(f"Enter {num_nodes} lines (one per node):")
    for i in range(num_nodes):
        line = input(f"Node {i+1}: ").strip()
        if not line:
            print("Empty line. Skipping...")
            continue
        
        # Split on colon, handle extra spaces
        if ':' not in line:
            print("Invalid format. Use 'node: neighbor1 neighbor2 ...'")
            continue
        
        node_part, neighbors_part = line.split(':', 1)
        node = node_part.strip()
        neighbors = [n.strip() for n in neighbors_part.split() if n.strip()]
        
        graph[node] = neighbors

    if not graph:
        print("No valid nodes entered.")
        return

    start = input("\nEnter the starting node: ").strip()
    
    if start not in graph:
        print(f"Error: Starting node '{start}' not in graph.")
        print("Available nodes:", list(graph.keys()))
        return
    
    print()
    bfs(graph, start)


# Run the program
if __name__ == "__main__":
    main()