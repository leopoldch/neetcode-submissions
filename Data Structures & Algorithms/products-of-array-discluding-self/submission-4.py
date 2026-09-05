class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)        
        product = 1
        for i, num in enumerate(nums):
            result[i] = product
            product *= num

        product = 1
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            result[i] *= product
            product *= num
        
        return result