from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        current_window_variables = defaultdict(int) #O(n)
        left, right = 0, 0

        longuest_str_replacement = 0
        max_freq = 0

        while right < len(s): # 0(n)
            current_caracter = s[right]
            current_window_variables[current_caracter] +=1
            max_freq = max(max_freq,current_window_variables[current_caracter] )
            
            while right - left+1 - max_freq > k:
                to_remove = s[left]
                current_window_variables[to_remove]  = max(current_window_variables[to_remove]-1,0)
                left+=1
            
            longuest_str_replacement = max(longuest_str_replacement, right-left+1)
            right+=1

        return longuest_str_replacement


