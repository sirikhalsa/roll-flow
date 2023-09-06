# vertex class which allows us to create graph vertices including functionality on adding edges to a vertex and getting stored
# edges from a vertex
class Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.position = (x, y)
        self.edges = {}

    def add_edge(self, vertex, weight = 0):
        self.edges[vertex] = weight

    def get_edges(self):
        return list(self.edges.keys())

    def get_weight(self, edge):
        return self.edges[edge]
