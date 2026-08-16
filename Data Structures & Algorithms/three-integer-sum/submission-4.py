class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        added = set()
        res = []
        for index, num in enumerate(sorted_nums):
            left = index+1
            right = len(sorted_nums)-1

            if num > 0:
                break

            while left < right:
                total = sorted_nums[left] + num + sorted_nums[right] 
                if total == 0:
                    candidate = sorted([num, sorted_nums[left], sorted_nums[right]])
                    key = "".join(str(candidate))
                    if key not in added:
                        res.append(candidate)
                        added.add(key)
                    left+=1
                elif total < 0:
                    left+=1
                else:
                    right-=1
        return res



