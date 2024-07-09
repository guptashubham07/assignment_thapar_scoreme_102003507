
def longest_path(graph: list) -> int:
    topo_order = topological_sort(graph)
    return calculate_longest_path(graph, topo_order)

def topological_sort(graph):
    n = len(graph)
    indeg = [0] * n
    for i in range(n):
        for j, w in graph[i]:
            indeg[j] += 1
    
    stack = [i for i in range(n) if indeg[i] == 0]
    topo_order = []
    
    while stack:
        node = stack.pop()
        topo_order.append(node)
        for neighbor, wt in graph[node]:
            indeg[neighbor] -= 1
            if indeg[neighbor] == 0:
                stack.append(neighbor)
    
    return topo_order

    
def calculate_longest_path(graph, topo_order):
    n = len(graph)
    dist = [-float('inf')] * n
    for node in topo_order:
        if dist[node] == -float('inf'):
            dist[node] = 0
        for neighbor, wt in graph[node]:
            if dist[node] + wt > dist[neighbor]:
                dist[neighbor] = dist[node] + wt
    
    return max(dist)

