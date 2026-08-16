class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        m = len(matrix)
        down = 0
        up = m-1

        while down <= up:
            mid = down + (up-down)//2
            val = matrix[mid][0]

            if val == target:
                return True

            if val > target:
                up = mid-1
            else:
                if mid == m-1 or matrix[mid+1][0] > target:
                    break
                
                down = mid+1

        line = down+(up-down)//2                
        
        n = len(matrix[0])
        left, right = 0, n-1

        while left <= right:
            mid = left + (right-left)//2

            val = matrix[line][mid]

            if val == target:
                return True
            
            if val < target:
                left = mid+1
            else:
                right = mid-1
            
        return False 





