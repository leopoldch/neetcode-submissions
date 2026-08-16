class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        n = len(nums)
        nbOccurences = 0

        currentIdx = 0
        for _ in range(n):
            if currentIdx >= len(nums):
                break
            
            if nums[currentIdx] == val:
                nbOccurences+=1
                nums.pop(currentIdx)
            else:
                currentIdx+=1

        return n-nbOccurences

