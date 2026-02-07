from BFS import bfs
from DFS import dfs
from GreedySearch import greedy
from AStar import Astar
from PerformanceTest import algorithms_100_runs_and_graphs, plot_graphs
from Heuristic import heuristic, heuristic2
import Algorithms
from List import map, sld_map
import numpy as np
import matplotlib.pyplot as plt

def main():
    
    while True:
        print("1. Breadth First Search ")
        print("2. Depth First Search ")
        print("3. Greedy First Search ")
        print("4. A* Search ")
        print("5. Performance Test (100 Runs) ")
        print("6. Exit ")
        
        choice = input("Enter your choice (1, 2, 3, 4, 5, or 6): ")
        
        match choice:
            # Breadth First Search
            case '1':
                bfs_start = input("Enter Starting City: ")
                bfs_goal = input("Enter the Goal City: ")
                
                path, expansions = bfs(bfs_start, bfs_goal, map)
                
                print("Path Found: ", path)
                print("Number of Expansions: ", expansions)
                continue
            # Depth First Search
            case '2':
                dfs_start = input("Enter Starting City: ")
                dfs_goal = input("Enter the Goal City: ")
                max_revisits = int(input("Enter maximum number of revisits: "))
                
                path, expansions = dfs(dfs_start, dfs_goal, map, max_revisits=max_revisits)
                
                print("Path found:", path)
                print("Number of expansions:", expansions)
                continue
            # Greedy First Search
            case '3':
                g_start = input("Enter Starting City: ")
                g_goal = input("Enter the Goal City: ")
                g_heuristic = str(input("Enter the heuristic to use (heuristic(SLD) or heuristic2(Scaled SLD)): "))
                
                if g_heuristic == "heuristic":
                    h = heuristic
                elif g_heuristic == "heuristic2":
                    h = heuristic2
                else:
                    print("Invalid Heuristic. ")
                    continue
                
                path, expansions = greedy(g_start, g_goal, map, h)
                
                print("Greedy path:", path)
                print("Nodes expanded:", expansions)
                continue
            # A* Search
            case '4':
                a_start = input("Enter Starting City: ")
                a_goal = input("Enter the Goal City: ")
                a_heuristic = input("Enter the heuristic to use (heuristic(SLD) or heuristic2(Scaled SLD)): ")
                
                if a_heuristic == "heuristic":
                    h = heuristic
                elif a_heuristic == "heuristic2":
                    h = heuristic2
                else:
                    print("Invalid Heuristic. ")
                    continue
                
                path, expansions = Astar(a_start, a_goal, map, h)
                
                print("Path found:", path)
                print("Number of expansions:", expansions)
                continue
            # Performance Test and Graphs
            case '5':
                p_start = input("Enter the Performance Test Start City: ")
                p_goal = input("Enter the Performance Test Goal City: ")
                
                (bfs_expan, bfs_time, dfs_expan, dfs_time, 
                greedyh1_expan, greedyh1_time, greedyh2_expan, greedyh2_time,
                astarh1_expan, astarh1_time, astarh2_expan, astarh2_time)= algorithms_100_runs_and_graphs(p_start, p_goal)
                
                
                plot_graphs(bfs_expan, bfs_time, "Breadth First Search Time Expansion")
                plot_graphs(dfs_expan, dfs_time, "Depth First Search Time Expansion")
                plot_graphs(greedyh1_expan, greedyh1_time, "Greedy First Search Heuristic 1 Time Expansion")
                plot_graphs(greedyh2_expan, greedyh2_time, "Greedy First Search Heuristic 2 Time Expansion")
                plot_graphs(astarh1_expan, astarh1_time, "A* Heuristic 1 Search Time Expansion")
                plot_graphs(astarh2_expan, astarh2_time, "A* Heuristic 2 Search Time Expansion")
                
                # Bar Chart of Average Time
                Test_time = ["BFS", "DFS", "GreedyH1", "GreedyH2", "A*H1", "A*H2"]
                average_time = [np.mean(bfs_time), np.mean(dfs_time), np.mean(greedyh1_time), 
                           np.mean(greedyh2_time), np.mean(astarh1_time), np.mean(astarh2_time)]
                plt.bar(Test_time, average_time, color=['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple'])
                plt.ylabel("Average Time (100 Runs)")
                plt.xlabel("Algorithms")
                plt.title("Algorithm Comparison: Time Average")
                plt.show()
                
                # Bar Chart of Average Node Expansion
                Test = ["BFS", "DFS", "GreedyH1", "GreedyH2", "A*H1", "A*H2"]
                average = [np.mean(bfs_expan), np.mean(dfs_expan), np.mean(greedyh1_expan), 
                           np.mean(greedyh2_expan), np.mean(astarh1_expan), np.mean(astarh2_expan)]
                plt.bar(Test, average, color=['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple'])
                plt.ylabel("Average Node Expansion (100 Runs)")
                plt.xlabel("Algorithms")
                plt.title("Algorithm Comparison: Node Expansion Average")
                plt.show()
                continue
            # Exit
            case '6':
                break
    
    
if __name__ == "__main__":
    main()