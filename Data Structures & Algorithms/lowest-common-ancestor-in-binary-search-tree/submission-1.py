# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.lowestAncestor = -1

        def explore(root):
            
            if not root:return False

            isInLeft = explore(root.left)
            isinRight = explore(root.right)

            if self.lowestAncestor != -1: # we already found
                return

            if isInLeft and isinRight:
                self.lowestAncestor = root
                return
            
            if (isInLeft or isinRight) and root.val in [p.val,q.val]:
                self.lowestAncestor = root
                return

            if root.val in [p.val,q.val]:
                return True

            return isInLeft or isinRight

        explore(root)

        return self.lowestAncestor