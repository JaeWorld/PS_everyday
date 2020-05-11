# Leetcode 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            tmp = target - num
            if tmp in d:
                return [d[tmp], i]
            else:
                d[num] = i
                
            
