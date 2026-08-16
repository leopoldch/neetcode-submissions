class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sorted_array = sorted(nums)
        res = []
        solutions = set()

        for index, num in enumerate(sorted_array):

            if num > 0:
                break

            left = index+1
            right = len(nums)-1

            while left<right:

                number_left = sorted_array[left]
                number_r = sorted_array[right]

                if number_r+number_left+num == 0 and (number_r, number_left, num) not in solutions:
                    solutions.add((number_r, number_left, num))
                    res.append([number_r, number_left, num])
                
                if number_r+number_left+num > 0:
                    right-=1
                else:
                    left+=1
        
        return res
