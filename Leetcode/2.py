# Leetcode 2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ret = ListNode(0)
        carry = 0
        
        while l1 or l2 or carry:
            temp = carry
            if l1:
                temp += l1.val
                l1 = l1.next
            if l2:
                temp += l2.val
                l2 = l2.next
                
            carry, temp = divmod(temp, 10)
            
            ret.next = ListNode(temp)
            ret = ret.next
            
        return ans.next
