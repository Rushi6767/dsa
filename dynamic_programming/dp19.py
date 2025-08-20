from typing import List
from collections import deque, defaultdict
import math

class Solution:
    def maxWeightedPath(self, n: int, weights: List[int], k: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        
        # DP table: dp[node][edges_used] = max_weight
        dp = [[-math.inf] * (k + 1) for _ in range(n)]
        
        # Base case: start at node 0 with 0 edges used
        dp[0][0] = weights[0]
        
        # Since it's a DAG, we can process nodes in topological order
        # For simplicity, we'll use BFS approach with DP state
        
        # We'll use a queue: (node, edges_used, current_weight)
        # But since we have DP table, we can process systematically
        
        # Alternative: iterate through all possible edge counts
        for edges_used in range(k + 1):
            for node in range(n):
                if dp[node][edges_used] == -math.inf:
                    continue
                
                # Try all neighbors
                for neighbor in graph[node]:
                    if edges_used + 1 <= k:
                        new_weight = dp[node][edges_used] + weights[neighbor]
                        if new_weight > dp[neighbor][edges_used + 1]:
                            dp[neighbor][edges_used + 1] = new_weight
        
        # Check all possibilities to reach node n-1 with at most k edges
        result = max(dp[n-1])
        return result if result != -math.inf else -1

# Test the solution
def test_solution():
    sol = Solution()
    
    # Test case 1
    n = 5
    weights = [2, -1, 3, 4, 5]
    k = 3
    edges = [[0,1], [0,2], [1,3], [2,3], [3,4]]
    
    result = sol.maxWeightedPath(n, weights, k, edges)
    print(f"Test 1: {result} (Expected: 14)")
    
    # Test case 2 - More complex
    n = 6
    weights = [10, -5, 8, 15, -3, 20]
    k = 4
    edges = [[0,1], [0,2], [1,3], [2,3], [3,4], [3,5], [4,5]]
    
    result = sol.maxWeightedPath(n, weights, k, edges)
    print(f"Test 2: {result}")

if __name__ == "__main__":
    test_solution()