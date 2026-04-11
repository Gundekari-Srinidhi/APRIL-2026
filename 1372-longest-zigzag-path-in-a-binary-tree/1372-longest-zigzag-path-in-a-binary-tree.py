# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        max1=0
        def order(node,last_direction,curr):
            nonlocal max1
            if not node:
                return
            max1=max(max1,curr)
            if node.left:
                if last_direction=="right":
                    order(node.left,"left",curr+1)
                else:
                    order(node.left,"left",1)
            if node.right:
                if last_direction=="left":
                    order(node.right,"right",curr+1)
                else:
                    order(node.right,"right",1)
        order(root,"",0)
        return max1
        