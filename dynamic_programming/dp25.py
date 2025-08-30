"""
122. Best Time to Buy and Sell Stock II
"""
from typing import List

class Solution:
    def solve(self, index, buy, prices):
        if index == len(prices):
            return 0

        if buy == 1:
            buy = -prices[index] + self.solve(index + 1, 0, prices)
            not_buy = 0 + self.solve(index + 1, 1, prices)
            profit = max(buy, not_buy)
        else:
            sell = prices[index] + self.solve(index + 1, 1, prices)
            not_sell = 0 + self.solve(index + 1, 0, prices)
            profit = max(sell, not_sell)
        return profit

    def maxProfit(self, prices: List[int]) -> int:
        return self.solve(0, 1, prices)
        
prices = [7,1,5,3,6,4]
s = Solution()
# print(s.maxProfit(prices))

"""
Time complexity : O(2^n)
Space complexity : O(n)  : stack space
"""

"""
2. Memoization [Top - Down]
"""

from typing import List

class Solution:
    def solve(self, index, buy, prices, dp):
        if index == len(prices):
            return 0
        
        if dp[index][buy] != -1:
            return dp[index][buy]

        if buy == 1:
            buy_p = -prices[index] + self.solve(index + 1, 0, prices, dp)
            not_buy = 0 + self.solve(index + 1, 1, prices, dp)
            profit = max(buy_p, not_buy)
        else:
            sell = prices[index] + self.solve(index + 1, 1, prices, dp)
            not_sell = 0 + self.solve(index + 1, 0, prices, dp)
            profit = max(sell, not_sell)
        dp[index][buy] = profit
        return dp[index][buy]

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # make N X 2 dp
        dp = [[-1, -1] for _ in range(n)]
        return self.solve(0, 1, prices, dp)
        
prices = [7,1,5,3,6,4]
s = Solution()
# print(s.maxProfit(prices))

"""
Time complexity : O(2n)
Space complexity : O(n)  + O(2 X N)
ss + dp
"""

"""
3. Tabulation [Bottom - Up]
"""

from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # make N X 2 dp
        dp = [[-1, -1] for _ in range(n + 1)]
        dp[n][0] = 0
        dp[n][1] = 0

        for index in range(n-1, -1, -1):
            for buy in range(0,2):
                if buy == 1:
                    buy_p = -prices[index] + dp[index+1][0]
                    not_buy = 0 + dp[index+1][1]
                    profit = max(buy_p, not_buy)
                else:
                    sell = prices[index] + dp[index+1][1]
                    not_sell = 0 + dp[index+1][0]
                    profit = max(sell, not_sell)
                dp[index][buy] = profit

        return dp[0][1]

        
prices = [7,1,5,3,6,4]
s = Solution()
# print(s.maxProfit(prices))

"""
Time complexity : O(2n)
Space complexity : O(2 X N)
dp
"""


"""
4. Tabulation [Space Optimization]
"""

from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # make N X 2 dp
        prev = [0, 0]
        # prev[0] = 0
        # prev[1] = 0

        for index in range(n-1, -1, -1):
            curr = [-1, -1]
            for buy in range(0,2):
                if buy == 1:
                    buy_p = -prices[index] + prev[0]
                    not_buy = 0 + prev[1]
                    profit = max(buy_p, not_buy)
                else:
                    sell = prices[index] + prev[1]
                    not_sell = 0 + prev[0]
                    profit = max(sell, not_sell)
                curr[buy] = profit
            prev = curr

        return prev[1]

        
prices = [7,1,5,3,6,4]
s = Solution()
print(s.maxProfit(prices))

"""
Time complexity : O(2n)
Space complexity : O(4) == O(1)
"""