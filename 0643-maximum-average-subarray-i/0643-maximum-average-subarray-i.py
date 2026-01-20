class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg=0
        curr_sum=sum(nums[:k])
        max_sum=curr_sum
        for i in range (k,len(nums)):
            curr_sum=curr_sum-nums[i-k]+nums[i]
            max_sum=max(max_sum,curr_sum)
        avg=max_sum/k
        return avg