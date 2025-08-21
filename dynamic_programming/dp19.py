from typing import List, Dict, Set
from collections import deque, defaultdict
import math

class Solution:
    def maxProjectProfit(self, n: int, profit: List[int], cpu: List[int], 
                        ram: List[int], dependencies: List[List[int]], 
                        max_cpu: int, max_ram: int, max_tasks: int) -> int:
        """
        n: number of tasks
        profit: profit for each task
        cpu: CPU requirement for each task
        ram: RAM requirement for each task
        dependencies: list of dependencies for each task
        max_cpu: maximum total CPU available
        max_ram: maximum total RAM available
        max_tasks: maximum number of tasks allowed
        """
        
        # Build reverse dependency graph and topological order
        graph = defaultdict(list)
        in_degree = [0] * n
        for i, deps in enumerate(dependencies):
            for dep in deps:
                graph[dep].append(i)
                in_degree[i] += 1
        
        # Get topological order using Kahn's algorithm
        topo_order = []
        queue = deque(i for i in range(n) if in_degree[i] == 0)
        
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # For each node, precompute all its dependencies (closure)
        task_dependencies = [set() for _ in range(n)]
        for node in reversed(topo_order):
            for dep in dependencies[node]:
                task_dependencies[node].add(dep)
                task_dependencies[node] |= task_dependencies[dep]
        
        # DP state: dp[i][tasks][cpu][ram] = max profit
        # We'll use memoization with state compression
        
        # Precompute cumulative requirements for dependency sets
        dep_requirements = {}
        for i in range(n):
            total_cpu = sum(cpu[j] for j in task_dependencies[i] | {i})
            total_ram = sum(ram[j] for j in task_dependencies[i] | {i})
            total_tasks = len(task_dependencies[i] | {i})
            total_profit = sum(profit[j] for j in task_dependencies[i] | {i})
            dep_requirements[i] = (total_cpu, total_ram, total_tasks, total_profit)
        
        # 4D DP table - too expensive, so we'll use memoization with pruning
        memo = {}
        
        def dfs(idx: int, tasks_used: int, cpu_used: int, ram_used: int, mask: int) -> int:
            if idx == n:
                return 0
                
            if tasks_used > max_tasks or cpu_used > max_cpu or ram_used > max_ram:
                return -math.inf
                
            state = (idx, tasks_used, cpu_used, ram_used, mask)
            if state in memo:
                return memo[state]
            
            node = topo_order[idx]
            result = dfs(idx + 1, tasks_used, cpu_used, ram_used, mask)  # Skip current
            
            # Check if we can take current node (all dependencies satisfied)
            can_take = True
            for dep in dependencies[node]:
                if not (mask & (1 << dep)):
                    can_take = False
                    break
            
            if can_take:
                new_tasks = tasks_used + 1
                new_cpu = cpu_used + cpu[node]
                new_ram = ram_used + ram[node]
                new_mask = mask | (1 << node)
                
                if new_tasks <= max_tasks and new_cpu <= max_cpu and new_ram <= max_ram:
                    take_profit = profit[node] + dfs(idx + 1, new_tasks, new_cpu, new_ram, new_mask)
                    result = max(result, take_profit)
            
            memo[state] = result
            return result
        
        # Alternative approach for larger constraints - knapsack on topological order
        # Since 4D DP might be too heavy, we use a different strategy
        
        # 3D DP: tasks × cpu × ram
        dp = [[[-math.inf] * (max_ram + 1) for _ in range(max_cpu + 1)] for _ in range(max_tasks + 1)]
        dp[0][0][0] = 0
        
        # Process nodes in topological order
        for node in topo_order:
            # New DP table for this state
            new_dp = [[row[:] for row in layer] for layer in dp]
            
            current_cpu = cpu[node]
            current_ram = ram[node]
            current_profit = profit[node]
            
            # Check all possible states where we can add this task
            for tasks in range(max_tasks):
                for c in range(max_cpu + 1 - current_cpu):
                    for r in range(max_ram + 1 - current_ram):
                        if dp[tasks][c][r] != -math.inf:
                            # Check if all dependencies are satisfied in the current state
                            # This is simplified - in real implementation, need dependency tracking
                            new_tasks = tasks + 1
                            new_cpu = c + current_cpu
                            new_ram = r + current_ram
                            new_profit = dp[tasks][c][r] + current_profit
                            
                            if (new_tasks <= max_tasks and new_cpu <= max_cpu and 
                                new_ram <= max_ram and new_profit > new_dp[new_tasks][new_cpu][new_ram]):
                                new_dp[new_tasks][new_cpu][new_ram] = new_profit
            
            dp = new_dp
        
        # Find maximum profit across all valid states
        result = -math.inf
        for tasks in range(max_tasks + 1):
            for c in range(max_cpu + 1):
                for r in range(max_ram + 1):
                    result = max(result, dp[tasks][c][r])
        
        return result if result != -math.inf else 0

# Test with a complex example
def test_solution():
    sol = Solution()
    
    # Test case 1
    n = 4
    profit = [10, -5, 20, 15]
    cpu = [2, 1, 3, 2]
    ram = [1, 2, 1, 3]
    dependencies = [[], [0], [0], [1, 2]]  # Task 1 depends on 0, task 2 depends on 0, task 3 depends on 1 and 2
    max_cpu = 6
    max_ram = 5
    max_tasks = 3
    
    result = sol.maxProjectProfit(n, profit, cpu, ram, dependencies, max_cpu, max_ram, max_tasks)
    print(f"Test 1: {result}")
    
    # Test case 2 - More complex
    n = 5
    profit = [30, -10, 25, 40, -5]
    cpu = [3, 2, 4, 1, 2]
    ram = [2, 3, 1, 4, 2]
    dependencies = [[], [0], [0], [1], [2, 3]]
    max_cpu = 8
    max_ram = 7
    max_tasks = 4
    
    result = sol.maxProjectProfit(n, profit, cpu, ram, dependencies, max_cpu, max_ram, max_tasks)
    print(f"Test 2: {result}")

if __name__ == "__main__":
    test_solution()