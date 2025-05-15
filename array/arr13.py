"""
121, Stock Buy and Sell
"""
# prices = [7,1,5,3,6,4]
prices =[7,6,4,3,1]
buy = prices[0]
profit = 0
sell = prices[-1]

for i in range(1, len(prices)):
    if prices[i] < buy:
        buy = prices[i]

    profit = max(profit, prices[i] - buy)

print(profit)

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
            
            profit = max(profit, p - buy_price)
        
        return profit
    
"""
Time complexity: O(n)
Space complexity: O(1)
"""