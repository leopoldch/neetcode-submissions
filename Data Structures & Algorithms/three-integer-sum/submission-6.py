class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        added = set()
        res = []
        for index, num in enumerate(sorted_nums):
            if num > 0:
                break

            if index > 0 and num == sorted_nums[index-1]:
                continue

            left = index+1
            right = len(sorted_nums)-1

            while left < right:
                total = sorted_nums[left] + num + sorted_nums[right] 
                if total == 0:
                    candidate = [num, sorted_nums[left], sorted_nums[right]]
                    res.append(candidate)
                    left+=1
                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1
                elif total < 0:
                    left+=1
                else:
                    right-=1
        return res



