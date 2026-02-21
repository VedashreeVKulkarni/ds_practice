class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        leftsum=0
        for i in range (len(nums)):
             total -= nums[i]  
             if leftsum == total:
              return i
             leftsum += nums[i]
        return -1

        
        