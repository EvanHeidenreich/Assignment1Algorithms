import heapq
from Heuristic import heuristic, heuristic2
from collections import deque
from Algorithms import Nodes
from List import map
from itertools import count

def greedy(start, goal, map, heuristic):
    # Initialize priority queue (heap) for nodes to explore
    queue = []
    # Counter to break ties in the heap when f-values are equal
    counter = count()
    # Add start node to heap with its heuristic value
    heapq.heappush(queue, (heuristic(start, goal), next(counter), Nodes(start, None, 0)))
    # Track visited cities
    visited = set()
    # Count node expansions
    expansions = 0

    while queue:
        # Pop node with lowest heuristic value
        _, _, current_node = heapq.heappop(queue)
        # Increment expansions counter
        expansions += 1
        # Get current city
        current_city = current_node.city
        # Check if goal reached
        if current_city == goal:
            return current_node.path(), current_node.g, expansions
        # Mark current city as visited
        visited.add(current_city)
        # Explore neighbors of current city
        for neighbor, cost in map.get(current_city, []):
            # Only consider unvisited neighbors
            if neighbor not in visited:
                # Create new node for neighbor
                child_node = Nodes(neighbor, current_node, current_node.g + cost)
                # Push neighbor to heap with its heuristic and counter
                heapq.heappush(queue, (heuristic(neighbor, goal), next(counter), child_node))

    # Return empty result if goal not found
    return [], 0, expansions