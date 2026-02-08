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

        for neighbor, cost in map[node.city]:
            if neighbor == goal:
                expansions += 1 
                return node.path() + [goal], node.g + cost, expansions

            if neighbor not in visited:
                visited.add(neighbor)
                fringe.append(Nodes(neighbor, node, node.g + cost))


    return [], 0 ,expansions