class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score=0
        stack=[0]
        for x in s:
         if x=='(':
            stack.append(0)
         else:    
            A=stack.pop()
            if A==0:
                score=1
            else:
                score=2*A
            stack[-1]+=score    
        return stack[-1]          
        