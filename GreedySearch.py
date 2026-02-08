import heapq
from Heuristic import heuristic, heuristic2
from collections import deque
from Algorithms import Nodes
from List import map
from itertools import count

def greedy(start, goal, map, heuristic):
    """
    Greedy Best-First Search using Nodes.g for cost
    Returns: path, total_cost, expansions
    """
    queue = []
    counter = count()  # tie-breaker for heapq
    heapq.heappush(queue, (heuristic(start, goal), next(counter), Nodes(start, None, 0)))
    visited = set()
    expansions = 0

    while queue:
        _, _, current_node = heapq.heappop(queue)
        expansions += 1
        current_city = current_node.city

        if current_city == goal:
            return current_node.path(), current_node.g, expansions

        visited.add(current_city)

        for neighbor, cost in map.get(current_city, []):
            if neighbor not in visited:
                child_node = Nodes(neighbor, current_node, current_node.g + cost)
                # Push (heuristic, counter, node) to avoid comparing Nodes
                heapq.heappush(queue, (heuristic(neighbor, goal), next(counter), child_node))

    return [], 0, expansions
