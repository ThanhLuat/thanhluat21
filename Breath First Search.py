def BFS(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


graph = defaultdict(list)
graph[1] = [2, 3]
graph[2] = [1, 4]
graph[3] = [1, 4]
graph[4] = [2, 3]