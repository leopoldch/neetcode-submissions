class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            try:
                indice = hashmap[diff]
                return [indice, i]
            except:
                hashmap[nums[i]] = i

        
        # shouldn't be coming there 



