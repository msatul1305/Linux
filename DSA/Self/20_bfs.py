from queue import Queue


def BFS(adj_list, root):
    distances = {}
    for node in adj_list:
        distances[node] = float('inf')
    distances[root] = 0
    visited = set()
    q = Queue()
    q.put(root)
    curr_dist = 1
    while q:
        # curr_q = list(q.queue)
        curr_visit_node = q.get()
        for node in adj_list[curr_visit_node]:
            # curr_q = list(q.queue)
            if node not in visited:
                q.put(node)
                curr_q = list(q.queue)
                distances[node] = distances[curr_visit_node] + 1
                visited.add(node)
        visited.add(curr_visit_node)
        curr_dist = curr_dist + 1
        if len(visited) == len(adj_list):
            break
    return distances


adjacency_list = {
    's': ['r', 'v', 'u'],
    'r': ['w', 't', 's'],
    't': ['r', 'u'],
    'u': ['t', 's', 'y'],
    'v': ['s', 'w', 'y'],
    'w': ['r', 'x', 'v', 'z'],
    'x': ['w', 'y', 'z'],
    'y': ['u', 'v', 'x'],
    'z': ['w', 'x']
}
print(BFS(adjacency_list, root='s'))
