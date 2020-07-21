# Leetcode 136. Single Number

# XOR 연산 => a, b가 같으면 0, 다르면 1

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            ans ^= nums[i]
        return ans
    
