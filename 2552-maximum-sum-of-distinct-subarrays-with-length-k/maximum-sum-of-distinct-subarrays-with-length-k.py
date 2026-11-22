class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        l = 0
        r = k - 1
        curr_sum = 0
        maxi = 0
        freq = {}
        for i in range(k):
            curr_sum+=nums[i]
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        if len(freq) == k:
                maxi =  curr_sum       
        for r in range(k, len(nums)): 
            curr_sum-=nums[l]       
            freq[nums[l]]-=1
            if freq[nums[l]] == 0:
                del freq[nums[l]]
            l+=1
            curr_sum+=nums[r]
            freq[nums[r]]=freq.get(nums[r],0)+1     
            if len(freq)==k:
                maxi=max(maxi,curr_sum)
        return maxi               