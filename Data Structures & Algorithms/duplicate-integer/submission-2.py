class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        viewed = set()

        for num in nums:
            if num in viewed:
                return True
            viewed.add(num)
        
        return False