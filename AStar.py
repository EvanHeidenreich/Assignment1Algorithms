import heapq
from Heuristic import heuristic, heuristic2
from List import map, sld_map

def Astar(start, goal, map, heuristic):
    queue = []
    heapq.heappush(queue, (heuristic(start, goal), 0, start, [start]))
    visited = {}
    expansions = 0
    
    while queue:
        f, g, node, path = heapq.heappop(queue)
        expansions += 1
        if node == goal:
            return path, expansions
        if node in visited and visited[node] <= g:
            continue
        
        visited[node] = g
        
        for neighbor, cost in map.get(node, []):
            new_g = g + cost
            new_f = new_g + heuristic(neighbor, goal)
            
            heapq.heappush(queue,(new_f, new_g, neighbor, path + [neighbor]))
    
    
    return [], expansions

# path, cost, expansions = Astar("Arad", "Bucharest", map, heuristic)

# print(path)
# print(cost)
# print(expansions)