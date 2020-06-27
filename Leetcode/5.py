# Leetcode 5. Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        res = ""
        maxLen = 0
        
        for i in range(n):
            lo1, len1 = self.extendPalindrome(s, i, i)
            lo2, len2 = self.extendPalindrome(s, i, i+1)
            if len1 > maxLen:
                maxLen = len1
                res = s[lo1:lo1+len1]
            if len2 > maxLen:
                maxLen = len2
                res = s[lo2:lo2+len2]
        
        return res
            
    def extendPalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        
        return l+1, r-l-1
