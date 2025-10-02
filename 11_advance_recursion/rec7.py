"""
Combination Sum 2
39
"""
# def backtrack(index, total, subset):
#     print(index, total, subset)
#     if total == k:
#         print("subset", subset)
#         d[len(subset)] = subset.copy()
#         return
#     if total > k:
#         return
#     elif index >= len(nums):
#         return
#     subset.append(nums[index])
#     sum1 = total + nums[index]
#     backtrack(index+1, sum1, subset)

#     subset.pop()
#     sum1 = total
#     backtrack(index+1, sum1, subset)

# nums = [1,1,2,1,2]
# d = {}
# k = 4
# backtrack(0,0, [])
# print(d.values())


# def backtrack(index, total, subset):
#     print(index, total, subset)
#     if total == k:
#         print("subset", subset)
#         j = tuple(sorted(subset))

#         result.add(j)
#         return
#     if total > k:
#         return
#     elif index >= len(nums):
#         return
#     subset.append(nums[index])
#     sum1 = total + nums[index]
#     backtrack(index+1, sum1, subset)

#     subset.pop()
#     sum1 = total
#     backtrack(index+1, sum1, subset)

# nums = [1,1,2,1,2]
# result = set()
# k = 4
# backtrack(0,0, [])
# print(result)


from typing import List

class Solution:
    def backtrack(self, subset: List[int], index: int, target: int, result: List[List[int]], candidates: List[int]):
        print(subset)
        if target == 0:
            result.append(subset.copy())  # Store valid subset
            return
        
        for i in range(index, len(candidates)):
            # Skip duplicates at the same recursion depth
            print(i, index)
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            # Prune the recursion tree if the current number exceeds the remaining target
            if candidates[i] > target:
                break
            
            # Include candidates[i] in the subset
            subset.append(candidates[i])
            self.backtrack(subset, i + 1, target - candidates[i], result, candidates)
            subset.pop()  # Backtrack (remove last element)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Sorting is crucial to handle duplicates
        result = []
        self.backtrack([], 0, target, result, candidates)
        return result

s = Solution()
output = s.combinationSum2([1, 1, 2, 1, 2], 4)
print(output)