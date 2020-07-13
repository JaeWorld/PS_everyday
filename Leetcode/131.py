# Leetcode 131. Palindrome Partitioning

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)                
        
        def func(s, res, idx, n):
            if idx == n:
                ans.append(res)
                return 
            
            n = len(s)
            for i in range(n):
                if s[:i+1] == s[i::-1]:
                    res.append(s[:i+1])
                    func(s[i+1:], res[:], i+1, n)
                    res.pop()
                    
        func(s, [], 0, n)
        return ans
