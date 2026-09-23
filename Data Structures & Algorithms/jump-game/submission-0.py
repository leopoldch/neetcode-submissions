class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_reachable = 0

        for i, num in enumerate(nums):
            if max_reachable < i:
                return False

            local_max = i+num
            max_reachable = max(local_max, max_reachable)

            if max_reachable >= len(nums)-1:
                return True
        
        if max_reachable >= len(nums)-1:
            return True
        return False