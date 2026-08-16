class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for expected in range(len(nums)):
            res = res ^ expected ^ nums[expected]
        return res

        


