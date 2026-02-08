import heapq
from Algorithms import Nodes
from Heuristic import heuristic, heuristic2
from List import map, sld_map

def Astar(start, goal, map, heuristic):

    # Priority queue: (f = g + h, counter, node)
    queue = []
    heapq.heappush(queue, (heuristic(start, goal), 0, Nodes(start)))

    visited = {}  # Dictionary to store visited cities and lowest g cost
    expansions = 0

    while queue:
        f, g, current_node = heapq.heappop(queue)
        expansions += 1
        current_city = current_node.city

        # Goal test
        if current_city == goal:
            return current_node.path(), current_node.g, expansions

        # If this city has been visited with lower cost, skip it
        if current_city in visited and visited[current_city] <= g:
            continue
        visited[current_city] = current_node.g

        # Expand neighbors
        for neighbor, cost in map[current_city]:
            new_g = g + cost
            new_f = new_g + heuristic(neighbor, goal)
            heapq.heappush(queue, (new_f, new_g, Nodes(neighbor, current_node, new_g)))

    return [], 0, expansions
