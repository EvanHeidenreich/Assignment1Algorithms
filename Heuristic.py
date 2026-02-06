from List import sld_map

def heuristic(city, goal):
    
    return abs(sld_map[city] - sld_map[goal])
    # if goal == "Bucharest":
    #     return sld_map[city]
    # else:
    #     return abs(sld_map[city] - sld_map[goal])
    
def heuristic2(city, goal):
    
    return abs(sld_map[city] - sld_map[goal]) * 0.5
    # if goal == "Bucharest":
    #     return sld_map[city]
    # else:
    #     return abs(sld_map[city] - sld_map[goal]) * 0.5