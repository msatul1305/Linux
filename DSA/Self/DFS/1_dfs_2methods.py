visited = []


def visit(i):
    for item in adjacency_list.get(i, None):
        if item and item not in visited:
            visited.append(item)
            visit(item)
        else:
            break


def dfs(adj):
    for key, val in adj.items():
        start_node = key
        next_nodes = val
        if start_node not in visited:
            visited.append(start_node)
            while next_nodes:
                i = next_nodes.pop()
                if i not in visited:
                    visited.append(i)
                    visit(i)
    return visited


adjacency_list = {
    'u': ['x', 'v'],
    'v': ['y'],
    'x': ['v'],
    'w': ['z', 'y'],
    'y': ['x'],
    'z': ['z'],
}

# adjacency_list = {
#     '1': ['2', '3', '4'],
#     '2': ['1', '3'],
#     '3': ['1', '2', '4'],
#     '4': ['1', '3', '5'],
#     '5': ['3', '4', '6', '7'],
#     '6': [''],
#     '7': [''],
# }

print(dfs(adjacency_list))
