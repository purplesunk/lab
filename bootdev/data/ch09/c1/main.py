class Graph:
    def adjacent_nodes(self, node):
        adj_nodes = []
        if self.graph[node]:
            for adj_node in self.graph[node]:
                adj_nodes.append(adj_node)
        return adj_nodes

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}
