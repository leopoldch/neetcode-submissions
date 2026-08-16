class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        car_seen = ""
        max_len = 0

        for car in s:
            if car in car_seen:
                max_len = max(max_len,len(car_seen))
                first_index = car_seen.find(car)
                car_seen = car_seen[first_index+1:]

            car_seen += car        
        return max(max_len,len(car_seen))
