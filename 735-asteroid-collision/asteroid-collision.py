class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack=[]
        for asteroid in asteroids:
            while stack and  stack[-1]>0 and asteroid<0:
                if abs(asteroid)>abs(stack[-1]):
                    stack.pop()    
                elif abs(stack[-1])>abs(asteroid):
                    break
                else:
                    stack.pop()
                    break
            else:
                stack.append(asteroid)
        return stack                   

    
        