class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        totalProduct = 1
        result = [0]*n

        for i in range(n):
            result[i] = totalProduct
            totalProduct *= nums[i]

        totalProduct = 1

        for i in range(n-1,-1,-1):
            result[i]*= totalProduct
            totalProduct *= nums[i]
        
        return result

