class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_part = []
        total_product = 1
        right_part = []

        for num in nums:
            total_product*=num
            left_part.append(total_product)
        total_product = 1
        for num in nums[::-1]:
            total_product*=num
            right_part.append(total_product)
        

        right_part = right_part[::-1]

        final = []

        def getVal(array, idx):
            if idx < 0 or idx >= len(array):
                return 1
            return array[idx]

        for i in range(len(nums)):
            i_left = i-1
            i_right = i+1
            final.append(getVal(left_part, i_left)*getVal(right_part, i_right))
        
        return final



            
        