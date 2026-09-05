class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        cache = {} # val -> index

        #for i, x in enumerate(nums):
        #    for j, y in enumerate(nums):
        #        if i == j:
        #            continue
        #        if x+y == target:
        #            return [i,j]
        
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in cache:
                return [cache[remaining], i]
            cache[num] = i
        

