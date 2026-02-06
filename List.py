# Weighted Adjaceny List

map = {
    "Arad": [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)],
    "Zerind": [("Arad", 75), ("Oradea", 71)],
    "Oradea": [("Zerind", 71), ("Sibiu", 151)],
    "Sibiu": [("Oradea", 151), ("Fagaras", 99), ("Rimnicu Vilcea", 80)],
    "Rimnicu Vilcea": [("Sibiu", 80), ("Pitesti", 97), ("Craiova", 146)],
    "Craiova": [("Pitesti", 138), ("Rimnicu Vilcea", 146), ("Drobeta", 120)],
    "Drobeta": [("Craiova", 120), ("Mehadia", 75)],
    "Mehadia": [("Drobeta", 75), ("Lugoj", 70)],
    "Lugoj": [("Mehadia", 70), ("Timisoara", 111)],
    "Timisoara": [("Lugoj", 111), ("Arad", 118)],
    "Fagaras": [("Sibiu", 99), ("Bucharest", 211)],
    "Pitesti": [("Rimnicu Vilcea", 97), ("Craiova", 138), ("Bucharest", 101)],
    "Bucharest": [("Fagaras", 211), ("Pitesti", 101), ("Giurgiu", 90), ("Urziceni", 85)],
    "Giurgiu": [("Bucharest", 90)],
    "Urziceni": [("Bucharest", 85), ("Vaslui", 142), ("Hirsova", 98)],
    "Hirsova": [("Urziceni", 98), ("Eforie", 86)],
    "Eforie": [("Hirsova", 86)],
    "Vaslui": [("Urziceni", 142), ("Iasi", 92)],
    "Iasi": [("Vaslui", 92), ("Neamt", 87)],
    "Neamt": [("Iasi", 87)]
}

sld_map = {
    'Arad': 366, 
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}