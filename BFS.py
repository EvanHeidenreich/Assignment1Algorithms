from collections import deque
from Algorithms import Nodes
from List import map


def bfs(start, goal, map):
    # Initialize queue with start node
    fringe = deque([Nodes(start)])
    # Track visited cities
    visited = {start}
    # Count node expansions
    expansions = 0

    while fringe:
        # Get next node from queue
        node = fringe.popleft()
        # Increment expansions
        expansions += 1

        # Explore neighbors
        for neighbor, cost in map[node.city]:
            # If goal found, return path, total cost, and expansions
            if neighbor == goal:
                expansions += 1
                return node.path() + [goal], node.g + cost, expansions

            # If neighbor not visited, mark and add to queue
            if neighbor not in visited:
                visited.add(neighbor)
                fringe.append(Nodes(neighbor, node, node.g + cost))

    # Return empty result if goal not found
    return [], 0, expansions