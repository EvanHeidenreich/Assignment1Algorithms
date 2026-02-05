from collections import deque
from Algorithms import Nodes
from List import map


def bfs(start, goal, map):
    fringe = deque([Nodes(start)])
    visited = {start}
    expansions = 0

    while fringe:
        node = fringe.popleft()
        expansions += 1

        for neighbor, _ in map[node.city]:
            if neighbor == goal:
                expansions += 1 
                return node.path() + [goal], expansions

            if neighbor not in visited:
                visited.add(neighbor)
                fringe.append(Nodes(neighbor, node))


    return [], expansions

path, expansions = bfs("Arad", "Bucharest", map)

print("Path found:", path)
print("Number of expansions:", expansions)