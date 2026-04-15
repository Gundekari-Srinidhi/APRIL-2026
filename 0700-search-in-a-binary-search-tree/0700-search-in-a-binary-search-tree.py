# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def order(node,val):
            if not node:
                return
            if node.val == val:
                return node  
            elif val < node.val:
                return order(node.left,val)
            elif val > node.val:
                return order(node.right,val)       
        return order(root,val)
        