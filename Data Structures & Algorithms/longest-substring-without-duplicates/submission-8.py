
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currentWindowIndexs = {}
        left = 0
        maxSubString = 0

        for idx, char in enumerate(s):

            if char in currentWindowIndexs and currentWindowIndexs[char]>=left :
                left = currentWindowIndexs[char]+1
            
            currentWindowIndexs[char] = idx
            maxSubString = max(maxSubString, idx-left+1)
        
        return maxSubString