from List import sld_map, map

def heuristic(city, goal):
    
    return abs(sld_map[city] - sld_map[goal])
    # if goal == "Bucharest":
    #     return sld_map[city]
    # else:
    #     return abs(sld_map[city] - sld_map[goal])
    
def heuristic2(city, goal):
    best = 0
    for neighbor, dist in map[city]:
        h = abs(sld_map[neighbor] - sld_map[goal])
        if h > best:
            best = h
    return best
    
    #return abs(sld_map[city] - sld_map[goal]) * 0.5
    # if goal == "Bucharest":
    #     return sld_map[city]
    # else:
    #     return abs(sld_map[city] - sld_map[goal]) * 0.5