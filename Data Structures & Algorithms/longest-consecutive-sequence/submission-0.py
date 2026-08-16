from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numbers_set = set(nums)
        max_consecutive = 0

        for num in nums:
            if num-1 in numbers_set:
                continue
            
            local_max = 0
            current = num
            while current in numbers_set:
                current+=1
                local_max+=1
                max_consecutive = max(max_consecutive,local_max )

        return max_consecutive


