class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        sorted_s1 = sorted(s1) # O(len(s1))

        left = 0
        right = len(s1)-1
        sub_string = s2[:right+1]

        while right < len(s2): # O(len(s2))

            sub_string = s2[left:right+1]
            if sorted(sub_string) == sorted_s1: # O(len(s1))
                return True

            left+=1; right+=1
        
        # space complexity O(len(s1))
        # time complexity O(len(s2)*len(s1))

        return False