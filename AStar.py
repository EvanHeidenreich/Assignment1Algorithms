import heapq
from Algorithms import Nodes
from Heuristic import heuristic, heuristic2
from List import map, sld_map

def Astar(start, goal, map, heuristic):
    # Initialize priority queue (heap) for nodes to explore
    # Each entry: (f = g + h, g, node)
    queue = []
    # Add start node with its heuristic value
    heapq.heappush(queue, (heuristic(start, goal), 0, Nodes(start)))
    # Dictionary to track visited cities and lowest g-cost
    visited = {}
    # Count node expansions
    expansions = 0

    while queue:
        # Pop node with lowest f-value
        f, g, current_node = heapq.heappop(queue)
        # Increment expansions counter
        expansions += 1
        # Get current city
        current_city = current_node.city
        # Goal test
        if current_city == goal:
            return current_node.path(), current_node.g, expansions

        # Skip if this city has been visited with lower or equal g-cost
        if current_city in visited and visited[current_city] <= g:
            continue
        
        # Record lowest g-cost for current city
        visited[current_city] = current_node.g

        # Expand neighbors
        for neighbor, cost in map[current_city]:
            # Compute new path cost g and f = g + h
            new_g = g + cost
            new_f = new_g + heuristic(neighbor, goal)
            # Add neighbor to heap with f, g, and node
            heapq.heappush(queue, (new_f, new_g, Nodes(neighbor, current_node, new_g)))

    # Return empty result if goal not found
    return [], 0, expansions