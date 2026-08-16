class Solution:

    def __init__(self):
        self.skipped_one = False

    def validPalindrome(self, s: str) -> bool:

        if len(s) <=1:
            return True

        if len(s) == 2 and s[0] == s[1]:
            return True


        def isPal(idx1, idx2):

            if idx1 >= idx2:
                return True

            if s[idx1] != s[idx2]:
                if self.skipped_one:
                    return False
                self.skipped_one = True
                return isPal(idx1+1, idx2) or isPal(idx1, idx2-1)

            return isPal(idx1+1, idx2-1)

        return isPal(0,len(s)-1)

        