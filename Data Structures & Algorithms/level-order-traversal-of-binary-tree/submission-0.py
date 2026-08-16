# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:return []

        current_array = [[root.val]]

        arrayleft = self.levelOrder(root.left)
        arrayRight = self.levelOrder(root.right)
        len_left = len(arrayleft)
        len_right = len(arrayRight)
        
        for i in range(max(len_left, len_right)):
            if i >= len_left:
                arrayleft.append([])
            if i >= len_right:
                break

            arrayleft[i].extend(arrayRight[i])
        
        current_array.extend(arrayleft)

        return current_array






