# Leetcode 6. ZigZag Conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        height = 0
        ascending = True
        res = ["" for _ in range(numRows+1)]
                
        for i in range(len(s)):
            if ascending:
                if height == numRows:
                    ascending = False
                    height -= 1
                else:
                    height += 1
            else:
                if height == 1:
                    ascending = True
                    height += 1
                else:
                    height -= 1
                
            res[height] += s[i]
            
        return "".join(res)
