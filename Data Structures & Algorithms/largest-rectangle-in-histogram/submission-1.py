class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        max_viewed_height = 0

        for idx, height in enumerate(heights):
            left = idx-1
            surface = 1
            while left >= 0 and heights[left] >= height:
                left-=1
                surface+=1
            
            right = idx+1
            while right < len(heights) and heights[right] >= height:
                right+=1
                surface+=1

            local_max = height*surface

            max_viewed_height = max(max_viewed_height, local_max)
        
        return max_viewed_height

