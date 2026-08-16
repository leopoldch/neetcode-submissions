class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(c.lower() for c in s if c.isalnum())
        length = len(s)
        
        while length >= 2:
            first = s[0]
            last = s[length-1]

            if first != last:
                return False
            
            s = s[1:length-1]
            length -= 2

        return True


        

        
