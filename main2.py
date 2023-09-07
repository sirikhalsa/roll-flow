from heapq import heappop, heappush
from math import inf

def dijkstras(graph, start):
    paths_distances_steps = {}

    for vertex in graph:
        paths_distances_steps[vertex] = [start, inf, 2]

    paths_distances_steps[start][1] = 0
    vertices_to_explore = [(start, 0)]

    while vertices_to_explore:
        current_vertex, current_distance = heappop(vertices_to_explore)
        paths_distances_steps[current_vertex][2] += 1
        # print('Working through {} now...'.format(current_vertex))

        for neighbor, edge_weight in graph[current_vertex]:
            # print(neighbor, edge_weight)
            new_distance = current_distance + edge_weight
            new_path = paths_distances_steps[current_vertex][0] + ('-->{}'.format(neighbor))


            if new_distance < paths_distances_steps[neighbor][1]:
                paths_distances_steps[neighbor][1] = new_distance
                paths_distances_steps[neighbor][0] = new_path
                heappush(vertices_to_explore, (neighbor, new_distance))

    return paths_distances_steps

graph = {
        'A': [('B', 10), ('C', 3)],
        'C': [('D', 2)],
        'D': [('E', 10)],
        'E': [('A', 7)],
        'B': [('C', 3), ('D', 2)]
    }

graph2 = {
        'Top Guard': [('Top Side Control', 10), ('Top Half Guard', 3)],
        'Top Half Guard': [('Top Mount', 5), ('Top Side Control', 3)],
        'Top Mount': [('Armbar', 10)],
        'Armbar': [('Top Mount', 0)],
        'Top Side Control': [('Top Half Guard', 0), ('Top Mount', 2)]
    }

def dijkstras_target(graph, start, target):
    dijkstras_dict = dijkstras(graph, start)
    for key, val in dijkstras_dict.items():
        if key == target:
            print('The shortest path from {} to {} takes {} steps, has a difficulty rating of {} and follows the path: \n{}'.format(start, target, val[2], val[1], val[0]))
            return val

dijkstras_target(graph2,'Top Guard','Armbar')
