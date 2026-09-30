class Solution:
    def twoSum(self, nums, target):
        seen={}
        for i in range(len(nums)):
            num=target-nums[i]
            if num in seen:
             return[seen[num],i] 
            seen[nums[i]]=i   



