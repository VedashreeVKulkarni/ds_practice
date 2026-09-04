class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1={}
        map2={}
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            
            if s_char in map1 and map1[s_char] != t_char:
             return False
            elif t_char in map2 and map2[t_char] != s_char:
             return False
            map1[s_char]=t_char
            map2[t_char]=s_char
        return True     


        
        