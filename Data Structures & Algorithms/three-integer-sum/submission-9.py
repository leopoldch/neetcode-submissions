from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        viewed = defaultdict(int)
        result = set()

        for j in range(1, len(nums)-1):
            i = j-1
            viewed[nums[i]]+=1

            for k in range(j+1, len(nums)):
                needed  = -(nums[k]+nums[j])
                if needed in viewed:
                    sorted_res = sorted([needed, nums[j], nums[k]])
                    result.add(tuple(sorted_res))
            
        
        return [[x,y,z] for x,y,z in result]
