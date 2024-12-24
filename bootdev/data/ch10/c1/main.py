class Graph:
    def bfs_path(self, start, end):
        def in_tuple_list(val, tuples):
            found = False
            for tup in tuples:
                if val in tup:
                    found = True
            return found

        visited = []
        to_visit = [(start, None)]

        while to_visit:
            cur = to_visit.pop(0)
            visited.append(cur)
            sorted_neighbors = sorted(self.graph[cur[0]])
            if end in sorted_neighbors:
                visited.append((end, cur[0]))
                break
            for neighbor in sorted_neighbors:
                if (not in_tuple_list(neighbor, visited)
                    and not in_tuple_list(neighbor, to_visit)):
                    to_visit.append((neighbor, cur[0]))

        if not in_tuple_list(end, visited):
            return None

        parent = None
        shortest_path = []
        for i in range(len(visited) - 1, -1, -1):
            if i == len(visited) - 1 or visited[i][0] == parent:
                shortest_path.append(visited[i][0])
                parent = visited[i][1]
        return shortest_path[::-1]

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result

