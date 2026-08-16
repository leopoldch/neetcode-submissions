class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        prev = nums[0]
        secprev = nums[nums[0]]

        while prev != secprev:
            prev = nums[prev]
            secprev = nums[nums[secprev]]

        prev = 0
        while prev != secprev:
            prev = nums[prev]
            secprev = nums[secprev]

        return prev
