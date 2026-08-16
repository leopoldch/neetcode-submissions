class Solution:
    def trap(self, height: List[int]) -> int:
        
        total = 0

        left = 0
        right = len(height)-1
        max_left = 0
        max_right = 0

        while left < right:
            height_left = height[left]
            height_right = height[right]
            max_left = max(height_left, max_left)
            max_right = max(height_right, max_right)

            if height_left < height_right:
                total += min(max_left, max_right) - height_left
                left+=1
            else:
                total += min(max_left, max_right) - height_right
                right-=1
        
        return total