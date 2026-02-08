from collections import deque
from Algorithms import Nodes
from List import map

def dfs(start, goal, map, max_revisits=None):
    # Initialize stack with start node
    fringe = deque([Nodes(start)])
    
    # Track visited cities and their visit counts
    # Dictionary: city -> times visited
    visited = {start: 1} 
    
    # How many nodes have been popped/expanded
    expansions = 0  
    
    while fringe:
        # Pop node from stack
        node = fringe.pop()  
        # Increment expansions counter
        expansions += 1
        # Check if current node is goal
        if node.city == goal:  
            # Return path, cost, expansions
            return node.path(), node.g, expansions  
        
        # Iterate over neighbors in reverse order for DFS order
        for neighbor, cost in reversed(map.get(node.city, [])):
            # Number of times neighbor visited
            visits = visited.get(neighbor, 0)  
            # Unlimited revisits case
            if max_revisits is None: 
                # If not visited yet
                if neighbor not in visited:  
                    # Mark as visited
                    visited[neighbor] = 1  
                    # Add neighbor to front of deque (DFS stack behavior)
                    fringe.appendleft(Nodes(neighbor, node, node.g + cost))
                    
            else: 
                # Check visit count against limit
                if visits < max_revisits:
                    # Increment visit count
                    visited[neighbor] = visits + 1
                    # Add neighbor to front of deque (DFS stack behavior)
                    fringe.appendleft(Nodes(neighbor, node, node.g + cost))
                    
    # Goal not found, return empty result
    return [], 0, expansions
