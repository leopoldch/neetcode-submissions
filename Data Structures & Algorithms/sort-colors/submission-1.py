class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left, right = 0, len(nums)-1
        current = 0


        while current <= right:

            if nums[current] == 2:
                nums[current], nums[right] = nums[right], nums[current]
                right-=1
                continue
            
            if nums[current] == 0:
                nums[current], nums[left] = nums[left], nums[current]
                left+=1
            current+=1 # on a vu un 1
        

