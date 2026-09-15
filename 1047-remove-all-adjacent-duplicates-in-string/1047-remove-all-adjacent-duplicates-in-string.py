class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for x in s:
            if not stack or stack[-1]!=x:
                stack.append(x)
            else:
                stack.pop()
        return "".join(stack)         
        