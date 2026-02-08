from BFS import bfs
from DFS import dfs
from GreedySearch import greedy
from AStar import Astar
from PerformanceTest import algorithms_100_runs_and_graphs, plot_graphs
from Heuristic import heuristic, heuristic2
from Algorithms import Nodes
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
                
                path, cost, expansions = bfs(bfs_start, bfs_goal, map)
                
                print("Path Found: ", path)
                print("Cost:", cost)
                print("Number of Expansions: ", expansions)
                continue
            # Depth First Search
            case '2':
                dfs_start = input("Enter Starting City: ")
                dfs_goal = input("Enter the Goal City: ")
                max_revisits_input = input("Enter maximum number of revisits (leave blank for no limit): ")

                # If the user presses Enter, use None
                if max_revisits_input == "":
                    max_revisits = None
                else:
                    max_revisits = int(max_revisits_input)
                
                path, cost, expansions = dfs(dfs_start, dfs_goal, map, max_revisits=max_revisits)
                
                print("Path found:", path)
                print("Cost: ", cost)
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
                
                path, cost, expansions = greedy(g_start, g_goal, map, h)
                
                print("Greedy path:", path)
                print("Cost: ", cost)
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
                
                path, cost, expansions = Astar(a_start, a_goal, map, h)
                
                print("Path found:", path)
                print("Cost: ", cost)
                print("Number of expansions:", expansions)
                continue
            # Performance Test and Graphs
            case '5':
                p_start = input("Enter the Performance Test Start City: ")
                p_goal = input("Enter the Performance Test Goal City: ")
                case_5_performance_test(p_start, p_goal)
                results = algorithms_100_runs_and_graphs(p_start, p_goal)
                

                # Bar Chart of Average Time
                Test_time = ["BFS", "DFS", "GreedyH1", "GreedyH2", "A*H1", "A*H2"]
                average_time_ns = [np.mean(results["BFS"][2]), np.mean(results["DFS"][2]), np.mean(results["GreedyH1"][2]), 
                                   np.mean(results["GreedyH2"][2]), np.mean(results["A*H1"][2]), np.mean(results["A*H2"][2])]
                plt.bar(Test_time, average_time_ns, color=['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple'])
                plt.ylabel("Average Time (ns) over 100 Runs")
                plt.xlabel("Algorithms")
                plt.title("Algorithm Comparison: Average Time in Nanoseconds")
                plt.show()
                
                # Bar Chart of Average Node Expansion
                Test = ["BFS", "DFS", "GreedyH1", "GreedyH2", "A*H1", "A*H2"]
                average_expansions = [np.mean(results["BFS"][0]), np.mean(results["DFS"][0]), np.mean(results["GreedyH1"][0]), 
                                      np.mean(results["GreedyH2"][0]), np.mean(results["A*H1"][0]), np.mean(results["A*H2"][0])]
                plt.bar(Test, average_expansions, color=['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple'])
                plt.ylabel("Average Node Expansion (100 Runs)")
                plt.xlabel("Algorithms")
                plt.title("Algorithm Comparison: Node Expansion Average")
                plt.show()
                continue
            # Exit
            case '6':
                break
    
def case_5_performance_test(p_start, p_goal):
    results = algorithms_100_runs_and_graphs(p_start, p_goal)
    
    # Print cost (same for all runs)
    print("\n--- Performance Test Results ---")
    for alg_name in results:
        expan, time_ms, time_ns, cost = results[alg_name]
        print(f"\nAlgorithm: {alg_name}")
        print(f"Cost: {cost}")
        print(f"Average Nodes Expanded: {np.mean(expan):.2f}")
        print(f"Average Time (ms): {np.mean(time_ms):.6f}")
        print(f"Average Time (ns): {np.mean(time_ns):.2f}")

        plot_graphs(expan, time_ns, f"{alg_name} Performance (ns)")
    
if __name__ == "__main__":
    main()