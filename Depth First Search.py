
def dfs(graph, node):
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor)

graph = {
    'A': ['B', 'E'],
    'B': ['A', 'C', 'D'],
    'C': ['B'],
    'D': ['B'],
    'E': ['A', 'F', 'G'],
    'F': ['E'],
    'G': ['E']
}
