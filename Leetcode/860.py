# Leetcode 860. Lemonade Change

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = {5: 0, 10: 0}
        n = len(bills)
        
        for i in range(n):
            if bills[i] == 5:
                changes[5] += 1
            elif bills[i] == 10:
                if changes[5] == 0:
                    return False
                changes[5] -= 1
                changes[10] += 1
            elif bills[i] == 20:
                if changes[10] > 0 and changes[5] > 0:
                    changes[10] -= 1
                    changes[5] -= 1
                elif changes[10] == 0 and changes[5] >= 3:
                    changes[5] -= 3
                else:
                    return False
        return True
