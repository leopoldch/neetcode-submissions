from collections import defaultdict, Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left = 0
        right = 0

        first_cache = Counter(s1)
        cache = defaultdict(int)

        while right < len(s2): 
            cache[s2[right]]+=1
            
            if right-left > len(s1)-1:
                # do things here
                cache[s2[left]]-=1
                left+=1

            if s2[right] in first_cache and right-left+1 == len(s1):
                v = True
                for i in range(left, right+1):
                    if first_cache[s2[i]] != cache[s2[i]]:
                        v =False
                
                if v:
                    return True

            right+=1


        return False