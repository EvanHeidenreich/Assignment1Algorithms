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
    
    bfs_expan, bfs_time_ms, bfs_time_ns, bfs_cost = [], [], [], None
    dfs_expan, dfs_time_ms, dfs_time_ns, dfs_cost = [], [], [], None
    greedyh1_expan, greedyh1_time_ms, greedyh1_time_ns, greedyh1_cost = [], [], [], None
    greedyh2_expan, greedyh2_time_ms, greedyh2_time_ns, greedyh2_cost = [], [], [], None
    astarh1_expan, astarh1_time_ms, astarh1_time_ns, astarh1_cost = [], [], [], None
    astarh2_expan, astarh2_time_ms, astarh2_time_ns, astarh2_cost = [], [], [], None
    
    for _ in range(run):
        # BFS 100 runs tracking time(ms and ns), expansions, and cost
        start_ns = time.perf_counter_ns()
        path, cost, expansion = bfs(start, goal, map)
        end_ns = time.perf_counter_ns()
        bfs_expan.append(expansion)
        bfs_time_ns.append(end_ns - start_ns)
        bfs_time_ms.append((end_ns - start_ns) / 1000000)  # convert ns → ms
        if bfs_cost is None:
            bfs_cost = cost

        # DFS 100 runs tracking time(ms and ns), expansions, and cost
        start_ns = time.perf_counter_ns()
        path, cost, expansion = dfs(start, goal, map, max_revisits=None)
        end_ns = time.perf_counter_ns()
        dfs_expan.append(expansion)
        dfs_time_ns.append(end_ns - start_ns)
        dfs_time_ms.append((end_ns - start_ns) / 1000000)
        if dfs_cost is None:
            dfs_cost = cost

        # Greedy H1 100 runs tracking time(ms and ns), expansions, and cost
        start_ns = time.perf_counter_ns()
        path, cost, expansion = greedy(start, goal, map, heuristic)
        end_ns = time.perf_counter_ns()
        greedyh1_expan.append(expansion)
        greedyh1_time_ns.append(end_ns - start_ns)
        greedyh1_time_ms.append((end_ns - start_ns) / 1000000)
        if greedyh1_cost is None:
            greedyh1_cost = cost

        # Greedy H2 100 runs tracking time(ms and ns), expansions, and cost
        start_ns = time.perf_counter_ns()
        path, cost, expansion = greedy(start, goal, map, heuristic2)
        end_ns = time.perf_counter_ns()
        greedyh2_expan.append(expansion)
        greedyh2_time_ns.append(end_ns - start_ns)
        greedyh2_time_ms.append((end_ns - start_ns) / 1000000)
        if greedyh2_cost is None:
            greedyh2_cost = cost

        # A* H1 100 runs tracking time(ms and ns), expansions, and cost
        start_ns = time.perf_counter_ns()
        path, cost, expansion = Astar(start, goal, map, heuristic)
        end_ns = time.perf_counter_ns()
        astarh1_expan.append(expansion)
        astarh1_time_ns.append(end_ns - start_ns)
        astarh1_time_ms.append((end_ns - start_ns) / 1000000)
        if astarh1_cost is None:
            astarh1_cost = cost

        # A* H2 100 runs tracking time(ms and ns), expansions, and cost
        start_ns = time.perf_counter_ns()
        path, cost, expansion = Astar(start, goal, map, heuristic2)
        end_ns = time.perf_counter_ns()
        astarh2_expan.append(expansion)
        astarh2_time_ns.append(end_ns - start_ns)
        astarh2_time_ms.append((end_ns - start_ns) / 1000000)
        if astarh2_cost is None:
            astarh2_cost = cost

    return {
        "BFS": (bfs_expan, bfs_time_ms, bfs_time_ns, bfs_cost),
        "DFS": (dfs_expan, dfs_time_ms, dfs_time_ns, dfs_cost),
        "GreedyH1": (greedyh1_expan, greedyh1_time_ms, greedyh1_time_ns, greedyh1_cost),
        "GreedyH2": (greedyh2_expan, greedyh2_time_ms, greedyh2_time_ns, greedyh2_cost),
        "A*H1": (astarh1_expan, astarh1_time_ms, astarh1_time_ns, astarh1_cost),
        "A*H2": (astarh2_expan, astarh2_time_ms, astarh2_time_ns, astarh2_cost),
    }

# Function to plot the graphs used in the report and for users viewing when running the performance test.
def plot_graphs(expansions, time, name):
    fig, ax1 = plt.subplots()

    color = 'tab:blue'
    ax1.set_xlabel("Run Number")
    ax1.set_ylabel("Node Expansions", color=color)
    ax1.plot(range(1, len(expansions)+1), expansions, color=color, label='Expansions')
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel("Time (ns)", color=color)
    ax2.plot(range(1, len(time)+1), time, color=color, label='Time')
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title(f"{name} Performance over {len(expansions)} Runs")
    fig.tight_layout()
    plt.show()
        
        