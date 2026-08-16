class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n = len(t)
        left = 0
        

        for idx, char in enumerate(s):

            if char == t[left]:
                left+=1
                if left >= n:
                    return 0
        return n - left
