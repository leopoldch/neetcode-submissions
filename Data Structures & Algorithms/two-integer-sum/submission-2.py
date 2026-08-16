class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)

        for i in range(length):
            number = nums[i]

            for j in range(length-1, i-1, -1):
                if j == i:continue

                other_number = nums[j]

                if number+ other_number == target:
                    return [i,j]
        
        # shouldn't be coming there 



