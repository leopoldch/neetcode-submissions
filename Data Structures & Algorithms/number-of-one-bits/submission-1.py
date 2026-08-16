class Solution:
    def hammingWeight(self, n: int) -> int:
        nb = 0
        while n !=0:            
            if n%2==1:
                nb+=1
            n = n >> 1
        return nb
