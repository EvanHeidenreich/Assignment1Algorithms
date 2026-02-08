from List import sld_map, map
from BFS import bfs

# Straight-Line Distance (SLD) heuristic
def heuristic(city, goal):
    # Straight-line distance heuristic to Bucharest
    if goal == "Bucharest":
        return sld_map[city]
    # Approximate heuristic for other goals using difference in SLD
    else:
        return abs(sld_map[city] - sld_map[goal])


# Neighbor-Based One-Step Lookahead Heuristic
def heuristic2(city, goal):
    # Initialize best heuristic value
    best = 0
    # Check all neighbors of the current city
    for neighbor, dist in map[city]:
        # Heuristic estimate: neighbor's SLD minus edge distance
        h = sld_map[neighbor] - dist
        # Keep the largest heuristic value found
        if h > best:
            best = h
    # Return the best heuristic value among neighbors
    return best
