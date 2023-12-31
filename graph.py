# graph class which contains a dictionary of vertices in the graph. It can also be defined as directed (undirected as default)
class Graph:
    def __init__(self, directed = False):
        self.graph_dict = {}
        self.directed = directed

    # function to add a vertex to the dictionary
    def add_vertex(self, vertex):
        self.graph_dict[vertex.name] = vertex

    # function that employs the class method from the vertex class to add edges to vertices in the dictionary
    # def add_edge(self, from_vertex, to_vertex, weight = 0):
    #     self.graph_dict[from_vertex.name].add_edge(to_vertex.name, weight)
    #     if not self.directed:
    #         self.graph_dict[to_vertex.name].add_edge(from_vertex.name, weight)

    def add_edge(self, from_vertex, to_vertex, weight = 0):
        self.graph_dict[from_vertex.name].add_edge(to_vertex, weight)
        if not self.directed:
            self.graph_dict[to_vertex.name].add_edge(from_vertex, weight)

    # function to find a path from one vertex to another within the dictionary
    def find_path(self, start_vertex, end_vertex):
        start = [start_vertex]
        seen = {}
        while len(start) > 0:
            current_vertex = start.pop(0)
            seen[current_vertex] = True
            print("Visiting " + current_vertex)
            if current_vertex == end_vertex:
                return True
            else:
                vertices_to_visit = set(self.graph_dict[current_vertex].edges.keys())
                start += [vertex for vertex in vertices_to_visit if vertex not in seen]
            return False
