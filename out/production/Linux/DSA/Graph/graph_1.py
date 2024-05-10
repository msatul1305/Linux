class Graph:
    def __init__(self):
        self.graph = {
            'A': ['B'],
            'B': ['E'],
            'C': [],
            'D': ['B'],
            'E': ['C']
        }

    def add_vertex(self, e):
        self.graph.update({e: []})

    def add_edge(self, v1, v2):
        if v1 in self.graph:
            self.graph[v1].append(v2)
            print(f"connected {v1} to {v2}")
        else:
            print(f"Vertex {v1} not in graph")

    def delete_edge(self, v1, v2):
        # if self.graph[v1]
        if any(v2 in item for item in self.graph[v1]):
            self.graph[v1].remove(v2)


    def delete_vertex(self, v):
        pass

    def print_edge(self):
        # traversal => BFS/DFS
        for item, edge in self.graph.items():
            if edge:
                for e in edge:
                    print(f'{item} --> {e}')
            else:
                print(f'{item}')


obj = Graph()
# obj.print_edge()
obj.add_edge('A', 'D')
# obj.add_edge('K', 'L')
obj.add_vertex('K')
# obj.add_edge('K', 'A')
# obj.print_edge()
print(obj.graph)
obj.delete_edge('A', 'B')
print(obj.graph)
