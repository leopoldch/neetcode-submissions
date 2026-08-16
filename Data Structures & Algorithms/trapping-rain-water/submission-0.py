class Solution:
    def trap(self, height: List[int]) -> int:
        
        total = 0

        max_left = []
        c_max_left = 0
        for j in range(len(height)):
            c_max_left = max(c_max_left, height[j])
            max_left.append(c_max_left)

        max_right = []
        c_max_right = 0
        for j in range(len(height)-1, -1, -1):
            c_max_right = max(c_max_right, height[j])
            max_right.append(c_max_right)

        max_right = max_right[::-1]

        for index, height in enumerate(height):
            local_max = min(max_right[index], max_left[index])
            total += local_max-height
        
        return total