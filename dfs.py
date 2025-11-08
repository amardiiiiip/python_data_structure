def dfs(graph, start):
    visited = set()
    stack = [start]
    print("DFS Traversal Order:", end=" ")
   
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            # Push neighbors in reverse to match recursive DFS (left-first)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    print()

def main():
    print("Enter the graph as an adjacency list.")
    print("Format: 'node: neighbor1 neighbor2 ...' (one per line)")
    num_nodes = int(input("Enter number of nodes: "))
    graph = {}
    
    for _ in range(num_nodes):
        line = input().strip()
        if not line:
            continue
        if ':' not in line:
            print(f"Invalid line (missing ':'): {line}")
            return
        node_part, neighbors_part = line.split(':', 1)
        node = node_part.strip()
        neighbors = [n.strip() for n in neighbors_part.split() if n.strip()]
        graph[node] = neighbors
   
    start = input("Enter the starting node: ").strip()
   
    if start not in graph:
        print("Starting node not in graph.")
        return
   
    dfs(graph, start)

if __name__ == "__main__":
    main()