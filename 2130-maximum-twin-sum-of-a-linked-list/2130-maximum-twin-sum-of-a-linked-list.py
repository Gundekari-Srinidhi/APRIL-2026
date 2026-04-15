# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        node = head
        while node:
            stack.append(node.val)
            node = node.next
        max_sum = float("-inf")
        l = 0
        r = len(stack)-1
        while l < r:
            max_sum = max(max_sum,stack[l]+stack[r])
            l+=1
            r-=1
        return max_sum

        
        