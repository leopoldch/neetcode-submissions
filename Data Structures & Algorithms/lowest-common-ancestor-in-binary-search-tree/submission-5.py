# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:return None

        if root.val in (p.val, q.val):
            return root
        
        valueLeft = self.lowestCommonAncestor(root.left, p, q)
        valueRight = self.lowestCommonAncestor(root.right, p, q)

        if valueLeft and valueRight:
            return root
        
        return valueLeft if valueLeft else valueRight









