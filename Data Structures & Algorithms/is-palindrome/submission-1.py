class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        length = 0
        for car in s:
            if car.isalpha() or car.isdigit():
                new_s += car.lower()
                length +=1
        
        while length >= 2:
            first = new_s[0]
            last = new_s[length-1]

            if first != last:
                return False
            
            new_s = new_s[1:length-1]
            length -= 2

        return True


        

        
