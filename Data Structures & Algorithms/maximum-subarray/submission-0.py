class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = float("-inf")
        current_max = float("-inf")

        for item in nums:
            current_max = max(current_max+item, item)
            global_max = max(global_max, current_max)
        
        return global_max