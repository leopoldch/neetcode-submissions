# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:return 0

        max_seen = {"max":0}

        def explore(root):
            if not root:
                return 0
            
            valueRight = explore(root.right)
            valueLeft = explore(root.left)

            if not valueRight and not valueLeft: # leaf
                return 1
            
            max_seen["max"] = max(valueRight + valueLeft, max_seen["max"])

            return max(valueRight, valueLeft)+1

        explore(root)

        return max_seen["max"]

        
        