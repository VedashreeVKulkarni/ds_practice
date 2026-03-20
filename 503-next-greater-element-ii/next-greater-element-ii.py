class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        n=len(nums)
        result=[-1]*n
        for i in range(2*n):
            while stack and nums[i%n]>nums[stack[-1]]:
                idx=stack.pop()
                result[idx]=nums[i%n]
            if i<n:
                    stack.append(i%n)
        return result            
        