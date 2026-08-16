# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        

        def findAncestor(node, p, q):
            if not node:return None

            if node.val in (p.val, q.val):
                return node
            
            valueLeft = findAncestor(node.left, p, q)
            valueRight = findAncestor(node.right, p, q)

            if valueLeft and valueRight:
                return node
            
            if valueLeft:
                return valueLeft
            
            return valueRight

        return findAncestor(root, p, q)








