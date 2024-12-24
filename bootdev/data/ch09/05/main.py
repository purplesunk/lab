class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    # don't touch below this line

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False
