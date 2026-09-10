class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        def palindrome(l,r):
            count=0
            while l>=0 and r<len(s):
                if s[l]==s[r]:
                    count+=1
                    l-=1
                    r+=1
                else:
                    break 
            return count
        for i in range(len(s)):
            palindrome(i,i)
            count+=palindrome(i,i)   

            palindrome(i,i+1)
            count+=palindrome(i,i+1)
        return count    


            