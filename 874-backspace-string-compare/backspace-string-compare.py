class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
      def build_stack(string):
        stack=[]
        for x in string:
            if x=='#':
                if stack:
                    stack.pop()
            else:
                stack.append(x)
        return stack  
      stack_s=build_stack(s)
      stack_t=build_stack(t)
      return stack_s==stack_t                     