import heapq
from Heuristic import heuristic, heuristic2
from collections import deque
from Algorithms import Nodes
from List import map

def greedy(start, goal, map, heuristic):
    queue = []
    heapq.heappush(queue, (heuristic(start, goal), start, [start]))
    visited = set()
    visit_count = 0
    
    while queue:
        _, node, path = heapq.heappop(queue)
        visited.add(node)
        visit_count += 1
        
        if node == goal:
            return path, visit_count
        
        for neighbor, _ in map.get(node, []):
            if neighbor not in visited:
                heapq.heappush(queue, (heuristic(neighbor, goal), neighbor, path + [neighbor]))

    return [], visit_count

# path, expansions = greedy("Arad", "Bucharest", map, heuristic)

# print("Greedy path:", path)
# print("Nodes expanded:", expansions)