class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nbZeros, zeroIdx = 0, -1
        totalProduct = 1
        result = [0]*n

        for idx, num in enumerate(nums):

            if num == 0:
                nbZeros += 1
                zeroIdx = idx
            else:
                totalProduct *= num
            
            if nbZeros > 1:
                return result
            

        for idx, num in enumerate(nums):
            
            if nbZeros:
                if num == 0:
                    result[idx] = totalProduct
            else:
                result[idx] = int(totalProduct/num)
        
        return result

