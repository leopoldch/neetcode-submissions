class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        for car in s:
            if car in dict1:
                dict1[car] = dict1[car]+1
                continue
            
            dict1[car] = 1
        
        for car in t:
            if car in dict2:
                dict2[car] = dict2[car]+1
                continue
            
            dict2[car] = 1

        return dict1 == dict2

