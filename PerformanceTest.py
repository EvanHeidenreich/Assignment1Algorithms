from BFS import bfs
from DFS import dfs
from GreedySearch import greedy
from AStar import Astar
from Heuristic import heuristic, heuristic2
from List import map
import matplotlib.pyplot as plt
import time

def algorithms_100_runs_and_graphs(start, goal):
    run = 100
    bfs_expan, bfs_time = [], []
    dfs_expan, dfs_time = [], []
    greedyh1_expan, greedyh1_time = [], []
    greedyh2_expan, greedyh2_time = [], []
    astarh1_expan, astarh1_time = [], []
    astarh2_expan, astarh2_time = [], []
    
    for _ in range(run):
        # Breadth First Search
        start_time = time.perf_counter()
        _, expansion = bfs(start, goal, map)
        end_time = time.perf_counter()
        bfs_expan.append(expansion)
        bfs_time.append(end_time - start_time)
        # Depth First Search
        start_time = time.perf_counter()
        _, expansion = dfs(start, goal, map, max_revisits=None)
        end_time = time.perf_counter()
        dfs_expan.append(expansion)
        dfs_time.append(end_time - start_time)
        # Greedy Search Heuristic 1
        start_time = time.perf_counter()
        _, expansion = greedy(start, goal, map, heuristic)
        end_time = time.perf_counter()
        greedyh1_expan.append(expansion)
        greedyh1_time.append(end_time - start_time)
        # Greedy Search Heuristic 2
        start_time = time.perf_counter()
        _, expansion = greedy(start, goal, map, heuristic2)
        end_time = time.perf_counter()
        greedyh2_expan.append(expansion)
        greedyh2_time.append(end_time - start_time)        
        # A* Search Heuristic 1
        start_time = time.perf_counter()
        _, expansion = Astar(start, goal, map, heuristic)
        end_time = time.perf_counter()
        astarh1_expan.append(expansion)
        astarh1_time.append(end_time - start_time)
        # A* Search Heuristic 2
        start_time = time.perf_counter()
        _, expansion = Astar(start, goal, map, heuristic2)
        end_time = time.perf_counter()
        astarh2_expan.append(expansion)
        astarh2_time.append(end_time - start_time)        
        
    return (bfs_expan, bfs_time, dfs_expan, dfs_time, 
            greedyh1_expan, greedyh1_time, greedyh2_expan, greedyh2_time,
            astarh1_expan, astarh1_time, astarh2_expan, astarh2_time)
    
def plot_graphs(expansions, time, name):
    fig, ax1 = plt.subplots()

    color = 'tab:blue'
    ax1.set_xlabel("Run Number")
    ax1.set_ylabel("Node Expansions", color=color)
    ax1.plot(range(1, len(expansions)+1), expansions, color=color, label='Expansions')
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel("Time (s)", color=color)
    ax2.plot(range(1, len(time)+1), time, color=color, label='Time')
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title(f"{name} Performance over {len(expansions)} Runs")
    fig.tight_layout()
    plt.show()
        
        