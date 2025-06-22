visited = []


def dfs(curr):
    if curr not in visited:
        visited.append(curr)
        for v in adjacency_list[curr]:
            dfs(v)
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
#     '6': [],
#     '7': [],
# }

x = ''
for item in adjacency_list.keys():
    if item not in visited:
        x = dfs(item)
print(x)
