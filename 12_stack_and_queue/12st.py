"""
735. Asteroid Collision
"""
from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        result = []

        for i in range(n):
            if asteroids[i]>0:
                result.append(asteroids[i])

            else:
                while len(result) != 0 and result[-1] < abs(asteroids[i]) and result[-1] > 0:
                    result.pop()

                if len(result) != 0 and result[-1] == abs(asteroids[i]) :
                    result.pop()

                elif len(result) == 0 or result[-1] < 0:
                    result.append(asteroids[i])

        return result
    
s = Solution()
asteroids = [4,7,1,1,2,-3,17,15,-16]
print(s.asteroidCollision(asteroids))

"""
Time complexity: O(2n) == O(n)
Space complexity: O(n)
"""