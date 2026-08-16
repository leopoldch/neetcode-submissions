class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)

        if h < n:
            # not possible
            return 0
        
        max_pile = max(piles)

        if h == len(piles):
            return max_pile
        
        total = sum(piles)

        if h >= total:
            return 1
        
        def getTime(k):
            total_time = 0

            for pile in piles:
                total_time+= (pile + k - 1) // k
            return total_time



        left = 1
        right = max_pile

        res = max_pile

        while left <= right:
            rate = left + (right - left) // 2
            time = getTime(rate)

            if time <= h:
                res = rate
                right = rate - 1
            else:
                left = rate + 1
        
        return res


