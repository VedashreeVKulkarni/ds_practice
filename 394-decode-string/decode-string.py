class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        current=""
        num=0
        for x in s:
            if x.isdigit():
                num=num*10+int(x)
            elif x=="[":
                stack.append((num,current))
                num=0
                current=""
            elif x=="]":
                count,previous=stack.pop()
                current=previous+current*count
            else:
                current+=x    
        return current                    
        