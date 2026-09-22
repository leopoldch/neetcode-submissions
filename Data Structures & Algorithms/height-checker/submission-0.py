class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        sorted_heights = sorted(heights) # O(nlog(n))
        counter = 0
        for i in range(len(heights)):
            if sorted_heights[i] != heights[i]:
                counter+=1
        return counter