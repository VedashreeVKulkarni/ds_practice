class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for x in s:
            stack.append(x)
            if len(stack)>=2 and  (stack[-1]==')' and stack[-2]=='('):
                stack.pop()
                stack.pop()
        return len(stack)        
