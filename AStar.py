import heapq
from List import map, sld_map

def Astar(start, goal, map, heuristic):
    queue = []
    heapq.heappush(queue, (heuristic(start), 0, start, [start]))
    visited = {}
    
    
    
    return