class Solution:
    def validPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        def isPalindrome(i,j):
         while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
         return True
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1   
            else:
               return isPalindrome(i+1,j) or isPalindrome(i,j-1)
        return True
                             
    
        