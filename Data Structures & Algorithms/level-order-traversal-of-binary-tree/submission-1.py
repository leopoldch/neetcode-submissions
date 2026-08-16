# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return []
        
        levels = []
        currentExploringNodes = deque()
        currentExploringNodes.append(root)

        while currentExploringNodes:
            currentDepthValues = []
            nbNodes = len(currentExploringNodes)

            for _ in range(nbNodes):
                node = currentExploringNodes.popleft()
                currentDepthValues.append(node.val)
                if node.left:
                    currentExploringNodes.append(node.left)
                if node.right:
                    currentExploringNodes.append(node.right)

            levels.append(currentDepthValues)
        
        return levels