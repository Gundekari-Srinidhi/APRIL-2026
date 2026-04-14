# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
        
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        d = {}
        def order(node,level):
            if not node:
                return 
            if level not in d:
                d[level] = 0
            d[level]+=node.val
            order(node.left,level+1)
            order(node.right,level+1)

        order(root,1)
        sum1 = float("-inf")
        min_level = 1
        for k,v in d.items():
            if v > sum1:
                sum1 = v
                min_level = k
        return min_level 

        