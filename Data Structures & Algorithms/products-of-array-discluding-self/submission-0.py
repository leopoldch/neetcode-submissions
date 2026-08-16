class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        zero_indice = -1

        for i, num in enumerate(nums):
            if num == 0:
                if zero_indice != -1:
                    return [0 for _ in range(len(nums))]
                zero_indice = i

                continue
            
            product*=num
        
        if zero_indice != -1:
            result = []
            for i in range(len(nums)):
                if i == zero_indice:
                    result.append(product)
                else:
                    result.append(0)
            return result
        
        return [int(product/num) for num in nums]



            

