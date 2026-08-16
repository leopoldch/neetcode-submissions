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
        currentNodesToExplore = deque()
        currentNodesToExplore.append(root)

        levels = []

        while currentNodesToExplore:
            localArray = []
            nbNodes = len(currentNodesToExplore)

            for _ in range(nbNodes):
                node = currentNodesToExplore.popleft()
                localArray.append(node.val)
                if node.left:
                    currentNodesToExplore.append(node.left)
                if node.right:
                    currentNodesToExplore.append(node.right)
            levels.append(localArray)
        
        return levels
                    








