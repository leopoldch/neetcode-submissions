class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1

        max_water = 0

        while left < right:
            total = min(heights[left], heights[right])*(right-left)

            max_water = max(total, max_water)

            if heights[left] < heights[right]:
                left+=1
                continue
            
            right-=1
        
        return max_water
            
