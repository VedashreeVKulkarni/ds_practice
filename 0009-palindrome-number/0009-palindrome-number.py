class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)           # convert integer to string
        return s == s[::-1]  # check if reversed string is equal


        