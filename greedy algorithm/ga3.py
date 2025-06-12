"""
Lemonade Change
"""
from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five  = 0
        ten = 0
        n = len(bills)


        for i in range(n):
            if bills[i] == 5:
                five += 1

            elif bills[i] == 10:
                if five >= 1:
                    ten += 1
                    five -= 1
                else:
                    return False
                
            else:
                if five >= 1 and ten >= 1:
                    five -= 1
                    ten -= 1
                    
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
    
bills = [5,5,10,10,20]
s = Solution()
print(s.lemonadeChange(bills))

"""
Time complexity : O(n)
Space complexity : O(1)
"""