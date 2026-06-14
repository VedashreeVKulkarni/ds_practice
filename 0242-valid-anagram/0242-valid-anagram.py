class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freq={}
        for ch in s:
         if ch not in freq:
            freq[ch]=1
         else:
            freq[ch]+=1
        freq1={} 
        for ch in t:
            if ch not in freq1:
             freq1[ch]=1
            else:
             freq1[ch]+=1
        if freq==freq1:
            return True
        else:
            return False    

        