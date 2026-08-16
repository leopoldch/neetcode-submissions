class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        minStrLength = float("inf")
        for s in strs:
            minStrLength = min(len(s),minStrLength)
        
        prefix = ""

        for i in range(minStrLength):
            char = strs[0][i]

            for j in range(1,len(strs)):
                if strs[j][i] != char:
                    return prefix
            
            prefix += char
        
        return prefix
            
