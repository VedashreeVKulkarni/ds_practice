class Solution:
    def minLength(self, s: str) -> int:
        stack=[]
        for x in s:
            stack.append(x)
            if len(stack)>=2 and                                                                   (stack[-2]=='A' and stack[-1]=='B' or stack[-2]=='C' and stack[-1]=='D'):
                stack.pop()
                stack.pop()
        return len(stack)        
        