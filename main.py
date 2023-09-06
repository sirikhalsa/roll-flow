# roll flow will use an A* graph search algorithm to determine the most efficient route between grappling positions
# the vertices in the graph will represent positions
# the edges will represnt valid transition between positions and their weight will indicate the relative transition difficulty
# we will use a Euclidean heuristic for the A* algorithm so we will graph in (x,y) with diagonal movements

from graph import Graph
from vertex import Vertex
from math import inf, sqrt
from heapq import heappop, heappush

# import the graph and both vertices from the graph files below
# NOTE to add an import statement if I want to place the data base in a separate file


# select the appropriate heuristic below and be sure to comment the other out
# Manhattan Heuristic:
def heuristic(start, target):
    x_distance = abs(start.position[0] - target.position[0])
    y_distance = abs(start.position[1] - target.position[1])
    return x_distance + y_distance

# Euclidean Heuristic:
#def heuristic(start, target):
#  x_distance = abs(start.position[0] - target.position[0])
#  y_distance = abs(start.position[1] - target.position[1])
#  return sqrt(x_distance * x_distance + y_distance * y_distance)

def a_star(graph, start, target):
    print("Starting A* algorithm!")
    count = 0
    paths_and_distances = {}
    for vertex in graph:
        paths_and_distances[vertex] = [inf, [start.name]]

    paths_and_distances[start][0] = 0
    vertices_to_explore = [(0, start)]
    while vertices_to_explore and paths_and_distances[target][0] == inf:
        current_distance, current_vertex = heappop(vertices_to_explore)
        for neighbor, edge_weight in graph[current_vertex]:
            new_distance = current_distance + edge_weight + heuristic(neighbor, target)
            new_path = paths_and_distances[current_vertex][1] + [neighbor.name]

        if new_distance < paths_and_distances[neighbor][0]:
            paths_and_distances[neighbor][0] = new_distance
            paths_and_distances[neighbor][1] = new_path
            heappush(vertices_to_explore, (new_distance, neighbor))
            count += 1
            print("\nAt " + vertices_to_explore[0][1].name)

    print("Found a path from {0} to {1} in {2} steps: ".format(start.name, target.name, count), paths_and_distances[target][1])

    return paths_and_distances[target][1]

def dict_builder(graph):
    dict = {}
    for title,object in graph.graph_dict.items():
        dict[title] = set([(name, weight) for name, weight in object.edges.items()])
    return dict

def graph_builder(graph):
    dict = {}
    for name,vertex in graph.graph_dict.items():
        dict[vertex] = set([(vertex, weight) for vertex, weight in vertex.edges.items()])
    return dict

def print_graph(graph):
    for vertex in graph.graph_dict:
        print("")
        print(vertex + " connected to")
        vertex_neighbors = graph.graph_dict[vertex].edges
        if len(vertex_neighbors) == 0:
            print("No edges!")
        for adjacent_vertex in vertex_neighbors:
            print("=> " + adjacent_vertex.name)

bottom_guard = Vertex('Bottom Guard', 0, 0)
top_guard = Vertex('Top Guard', 0, 0)
bottom_half = Vertex('Bottom Half Guard', 0, 0)
top_half = Vertex('Top Half Guard', 0, 0)
bottom_side = Vertex('Bottom Side Control', 0, 0)
top_side = Vertex('Top Side Control', 0, 0)
bottom_mount = Vertex('Bottom Mount', 0, 0)
top_mount = Vertex('Top Mount', 0, 0)
bottom_back = Vertex('Bottom Back Control', 0, 0)
top_back = Vertex('Top Back Control', 0, 0)
armbar = Vertex('Armbar', 0, 0)
kimura = Vertex('Kimura', 0, 0)
americana = Vertex('Americana', 0, 0)
rear_naked = Vertex('Rear Naked Choke', 0, 0)

flow_map = Graph(True)
# add vertices
flow_map.add_vertex(bottom_guard)
flow_map.add_vertex(top_guard)
flow_map.add_vertex(bottom_half)
flow_map.add_vertex(top_half)
flow_map.add_vertex(bottom_side)
flow_map.add_vertex(top_side)
flow_map.add_vertex(bottom_mount)
flow_map.add_vertex(top_mount)
flow_map.add_vertex(bottom_back)
flow_map.add_vertex(top_back)
flow_map.add_vertex(armbar)
flow_map.add_vertex(kimura)
flow_map.add_vertex(americana)
flow_map.add_vertex(rear_naked)
# add edges
flow_map.add_edge(bottom_guard, top_mount, 0)
# flow_map.add_edge(bottom_guard, bottom_half, 0)
flow_map.add_edge(top_mount, armbar, 0)

# print_graph(flow_map)
flow_map_dict = graph_builder(flow_map)
# print(flow_map_dict)
a_star(flow_map_dict, bottom_guard, armbar)

#Test
#
# class graph_vertex:
#     def __init__(self, name, x, y):
#         self.name = name
#         self.position = (x, y)
#
# delhi = graph_vertex("New Delhi", 28.6448, 77.216721)
# jaipur = graph_vertex("Jaipur", 26.92207, 75.778885)
# varanasi = graph_vertex("Varanasi", 25.321684, 82.987289)
# mumbai = graph_vertex("Mumbai", 19.07283, 72.88261)
# chennai = graph_vertex("Chennai", 13.067439, 80.237617)
# hyderabad = graph_vertex("Hyderabad", 17.387140, 78.491684)
# kolkata = graph_vertex("Kolkata", 22.572645, 88.363892)
# bengaluru = graph_vertex("Bengaluru", 12.972442, 77.580643)
#
# euclidean_graph = {
#   delhi: set([(jaipur, 2.243918), (varanasi, 6.65902), (mumbai, 10.507479), (chennai, 15.867576), (hyderabad, 11.329626), (kolkata, 12.693718), (bengaluru, 15.676582)]),
#   jaipur: set([(mumbai, 8.366539), (delhi, 2.243918)]),
#   varanasi: set([(delhi, 6.65902), (mumbai, 11.88077)]),
#   mumbai: set([(delhi, 10.507479), (jaipur, 8.366539), (varanasi, 11.88077), (hyderabad, 5.856898), (kolkata, 15.87195), (bengaluru, 7.699756)]),
#   chennai: set([(delhi, 15.867576), (kolkata, 12.50541), (hyderabad, 4.659195), (bengaluru, 2.658671)]),
#   hyderabad: set([(delhi, 11.329626), (mumbai, 5.856898), (chennai, 4.659195), (bengaluru, 4.507721), (kolkata, 11.151231)]),
#   kolkata: set([(delhi, 12.693718), (mumbai, 15.87195), (chennai, 12.50541), (hyderabad, 11.151231), (bengaluru, 14.437532)]),
#   bengaluru: set([(delhi, 15.676582), (mumbai, 7.699756), (chennai, 2.658671), (hyderabad, 4.507721), (kolkata, 14.437532)])
# }
#

# print(euclidean_graph)
