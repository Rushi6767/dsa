"""
Floyd Warshall Algorithm (All-Pairs Shortest Path)
"""
class Solution:
    def floydWarshall(self, dist):
        n = len(dist)
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][via] != 10**8 and dist[via][j] != 10**8:
                        dist[i][j] = min(dist[i][j], dist[i][via] + dist[via][j])
        return dist
    
dist = [[0, 4, 10**8, 5, 10**8], [10**8, 0, 1, 10**8, 6], [2, 10**8, 0, 3, 10**8], [10**8, 10**8, 1, 0, 2], [1, 10**8, 10**8, 4, 0]]
S=Solution()
print(S.floydWarshall(dist))

"""
Time complexity : O(n**3)
Space complexity : O(n**2)
"""