"""
188. Best Time to Buy and Sell Stock IV
"""

from typing import List

class Solution:
    def solve(self, index, buy, prices, limit):
        if index == len(prices):
            return 0
        
        if limit == 0:
            return 0
        
        if buy == 1:
            buy_p = -prices[index] + self.solve(index+1, 0, prices, limit)
            not_buy = 0 + self.solve(index+1, 1, prices, limit)
            profit = max(buy_p, not_buy)
        else :
            sell = prices[index] + self.solve(index+1, 1, prices, limit-1)
            not_sell = 0 + self.solve(index+1, 0, prices, limit)
            profit = max(sell, not_sell)
        return profit
    def maxProfit(self, k: int, prices: List[int]) -> int:
        return self.solve(0, 1, prices, k)

k = 2
prices = [2,4,1]
s = Solution()
# print(s.maxProfit(k, prices))

"""
Time complexity : O(2^n)
Space complexity : O(n)  : stack space
"""

"""
2. Memoization [Top - Down]
"""
class Solution:
    def solve(self, index, buy, prices, limit, dp):
        if index == len(prices):
            return 0
        
        if limit == 0:
            return 0
        
        if dp[index][buy][limit] != -1:
            return dp[index][buy][limit]
        
        if buy == 1:
            buy_p = -prices[index] + self.solve(index+1, 0, prices, limit, dp)
            not_buy = 0 + self.solve(index+1, 1, prices, limit, dp)
            profit = max(buy_p, not_buy)
        else :
            sell = prices[index] + self.solve(index+1, 1, prices, limit-1, dp)
            not_sell = 0 + self.solve(index+1, 0, prices, limit, dp)
            profit = max(sell, not_sell)
        dp[index][buy][limit] = profit
        return dp[index][buy][limit]
    
    def maxProfit(self, k, prices: List[int]) -> int:
        n = len(prices)

        # index(n), buy(2), limit(3) == n X 2 X 3  == 3d DP
        # note: always start reverse(simple hack)
        dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]

        return self.solve(0, 1, prices, k, dp)


k = 2
prices = [2,4,1]
s = Solution()
# print(s.maxProfit(k, prices))

"""
Time complexity : O(2 X k X n)
Space complexity : O(n)  + O(2 X k X N)
ss + dp
"""

"""
3. Tabulation [Bottom - Up]
"""
class Solution:
    def maxProfit(self, k, prices: List[int]) -> int:
        n = len(prices)

        # index(n), buy(2), limit(3) == n+1 X 2 X 3  == 3d DP
        # note: always start reverse(simple hack)
        dp = [[[-1 for _ in range(k+1)] for _ in range(2)] for _ in range(n+1)]

        for buy in range(2):
            for limit in range(k+1):
                dp[n][buy][limit] = 0

        for index in range(n+1):
            for buy in range(2):
                dp[index][buy][0] = 0

        for index in range(n-1, -1, -1):
            for buy in range(2):
                for limit in range(1,k+1):
                    if buy == 1:
                        buy_p = -prices[index] + dp[index+1][0][limit]
                        not_buy = 0 + dp[index+1][1][limit]
                        profit = max(buy_p, not_buy)
                    else :
                        sell = prices[index] + dp[index+1][1][limit-1]
                        not_sell = 0 + dp[index+1][0][limit]
                        profit = max(sell, not_sell)
                    dp[index][buy][limit] = profit
        return dp[0][1][k]

k = 2
prices = [2,4,1]
s = Solution()
# print(s.maxProfit(k, prices))

"""
Time complexity : O(2 X k X n)
Space complexity : O(2 X k X N)
dp
"""



"""
4. Tabulation [Space Optimization]
"""
class Solution:
    def maxProfit(self, k, prices: List[int]) -> int:
        n = len(prices)
        prev = [[-1 for _ in range(k+1)] for _ in range(2)]

        for buy in range(2):
            for limit in range(k+1):
                prev[buy][limit] = 0

        for buy in range(2):
            prev[buy][0] = 0

        for index in range(n-1, -1, -1):
            curr = [[-1 for _ in range(k+1)] for _ in range(2)]
            for buy in range(2):
                for limit in range(0,k+1):
                    if limit == 0:
                        profit = 0
                    elif buy == 1:
                        buy_p = -prices[index] + prev[0][limit]
                        not_buy = 0 + prev[1][limit]
                        profit = max(buy_p, not_buy)
                    else :
                        sell = prices[index] + prev[1][limit-1]
                        not_sell = 0 + prev[0][limit]
                        profit = max(sell, not_sell)
                    curr[buy][limit] = profit
            prev = curr
        return prev[1][k]

k = 2
prices = [2,4,1]
s = Solution()
print(s.maxProfit(k, prices))


"""
Time complexity : O(2 X k X n)
Space complexity : prev = O(2 X k+1) + curr O(2 X k+1) = O(2 X k X 3) = O(1)
"""
