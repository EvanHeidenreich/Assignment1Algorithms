from collections import deque
from Algorithms import Nodes
from List import map

def dfs(start, goal, map, max_revisits=None):
    fringe = deque([Nodes(start)])
    visited = {start: 1}
    expansions = 0
    
    while fringe:
        node = fringe.popleft()
        expansions += 1
        
        if node.city == goal:
            return node.path(), expansions
        
        for neighbor, _ in reversed(map.get(node.city, [])):
            visits = visited.get(neighbor, 0)

            if max_revisits is None:
                if neighbor not in visited:
                    visited[neighbor] = 1
                    fringe.appendleft(Nodes(neighbor, node))
            else:
                if visits < max_revisits:
                    visited[neighbor] = visits + 1
                    fringe.appendleft(Nodes(neighbor, node))
                    
    return [], expansions

path, expansions = dfs("Arad", "Bucharest", map, max_revisits=4)

print("Path found:", path)
print("Number of expansions:", expansions)