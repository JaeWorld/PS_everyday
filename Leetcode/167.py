# Leetcode 167. Two Sum II - Input array is sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        length = len(numbers)
        
        for i in range(length):
            dic[numbers[i]] = i
        
        for i in range(length):
            nxt = target - numbers[i]
            if nxt in dic:
                return [i+1, dic[nxt]+1]
                
