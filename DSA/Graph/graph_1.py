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
        self.graph.update({e: [""]})

    def add_edge(self, v1, v2):
        if v1 in self.graph:
            self.graph[v1].append(v2)
            print(f"connected {v1} to {v2}")
        else:
            print(f"Vertex {v1} not in graph")

    def print_edge(self):
        # traversal => BFS/DFS
        for item, edge in self.graph.items():
            for e in edge:
                if e != '':
                    print(f'{item}-->{e}')
                else:
                    print(f'{item}')
            # print(item, edge)


obj = Graph()
# obj.print_edge()
obj.add_edge('A', 'D')
# obj.add_edge('K', 'L')
obj.add_vertex('K')
obj.add_edge('K', 'A')
# TODO: check for this error - K printing twice
obj.print_edge()
print(obj.graph)
