from List import sld_map, map
from BFS import bfs

def heuristic(city, goal):
    if goal == "Bucharest":
        return sld_map[city]
    else:
        return abs(sld_map[city] - sld_map[goal])

def heuristic2(city, goal):
    # Pick the smallest SLD among neighbors — always underestimates
    min_h = float('inf')
    for neighbor, _ in map[city]:
        h = abs(sld_map[neighbor] - sld_map[goal])
        if h < min_h:
            min_h = h
    return min_h
    
    #return abs(sld_map[city] - sld_map[goal]) * 0.5
    # if goal == "Bucharest":
    #     return sld_map[city]
    # else:
    #     return abs(sld_map[city] - sld_map[goal]) * 0.5