# Dijkstra algorithm
# - Djikstra algorithm allows us to find the shortest path between starting vertex to all vertices in a graph
# 
#
# Steps
# 1) Pick starting node
# 2) Initialize table of distances
# 3) Examine edges leaving starting vertex
# 3) Update the distance to those vertices
# 4) Pick the smallest edge/distances of which the vertex hasnt been chosen
# 5) Cross the visited node in the unvisited node
# 6) Examine the current node, looking for all edges, then choose the smallest one
# 7) Repeat for all unvisited node

import heapq

def dijkstra(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0
    pq = [(0, starting_vertex)]

    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances


graph = {
    'A': {'B':2, 'C': 6},
    'B': {'D':5},
    'C': {'D':8},
    'D':{},
    
}

print(dijkstra(graph, 'A'))
print(graph['A'].items())