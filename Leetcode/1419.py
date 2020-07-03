# Leetcode 1419. Minimum Number of Frogs Croaking

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        cnt = [0]*5
        s = 'croak'
        l = len(croakOfFrogs)
        frogs = 0
        ans = 0
        
        for i in range(l):
            idx = s.index(croakOfFrogs[i])
            cnt[idx] += 1
            if idx == 0:
                frogs += 1
                ans = max(ans, frogs)
            elif idx == 4:
                frogs -= 1
            else:
                cnt[idx-1] -= 1
                if cnt[idx-1] < 0:
                    return -1
            
        return ans if not frogs else -1
