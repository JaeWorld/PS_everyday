# Leetcode 3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        res = 0
        temp = ""
        
        while end < len(s):
            if s[end] not in temp:
                temp = s[start:end+1]
                end += 1
            else:
                while True:
                    if s[end] not in temp:
                        break
                    start += 1
                    temp = s[start:end]
            res = max(res, len(temp))
            
        return res
                
