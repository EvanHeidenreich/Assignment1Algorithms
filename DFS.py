from collections import deque
from Algorithms import Nodes
from List import map

def dfs(start, goal, map, max_revisits=None):
    fringe = deque([Nodes(start)])
    visited = {start: 1}    
    expansions = 0
    
    while fringe:
        node = fringe.pop()
        expansions += 1
        
        if node.city == goal:
            return node.path(), node.g, expansions
        
        for neighbor, cost in reversed(map.get(node.city, [])):
            visits = visited.get(neighbor, 0)

            if max_revisits is None:
                if neighbor not in visited:
                    visited[neighbor] = 1
                    fringe.appendleft(Nodes(neighbor, node, node.g + cost))
            else:
                if visits < max_revisits:
                    visited[neighbor] = visits + 1
                    fringe.appendleft(Nodes(neighbor, node, node.g + cost))
                    
    return [], 0, expansions
