class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        answer=""
        remove=set()
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            elif s[i]==")":
                if stack:
                    stack.pop()
                else:
                    remove.add(i)
        remove.update(stack)
        for i in range(len(s)):
            if i not in remove:
                answer+=s[i]
        return answer                    


        