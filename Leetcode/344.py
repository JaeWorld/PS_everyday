# Leetcode 344. Reverse String

class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        for i in range(n//2):
            temp = s[n-1-i]
            s[n-1-i] = s[i]
            s[i] = temp
            
