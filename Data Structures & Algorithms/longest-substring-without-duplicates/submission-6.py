class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {} # Stocke char -> index
        max_len = 0
        start = 0 # Début de la fenêtre
        
        for i, car in enumerate(s):
            # Si on a déjà vu le caractère et qu'il est DANS la fenêtre actuelle
            if car in char_map and char_map[car] >= start:
                start = char_map[car] + 1
            
            char_map[car] = i
            max_len = max(max_len, i - start + 1)
            
        return max_len