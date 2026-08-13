class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        seen={}
        expected=n*(n+1)//2
        actual=sum(nums)
        duplicate = None 
        for num in nums:
            if num not in seen:
               seen[num] = 1
            else:   
                duplicate=num
        missing=expected-actual+duplicate
        return [duplicate,missing]        
        